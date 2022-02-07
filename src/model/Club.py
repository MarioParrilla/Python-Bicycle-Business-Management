from src.model.Partner import *
from src.model.Fee import Fee
from src.core import Persistence
from datetime import date, datetime

class Club:

    def __init__(self, name: str, cif: str, socialBase: str):
        self.name = name
        self.cif = cif
        self.socialBase = socialBase
        self.listOfUsers = None
        self.listOfEvents = None
        self.totalBalance = 0
        self.listOfFees = None

    def init(self, dniUserLogin: str):
        data = Persistence.init()
        self.listOfUsers = data[0]
        self.listOfFees = data[1]

        user = self.listOfUsers.get(dniUserLogin)
        user.lastAccess = str(datetime.today())
        self.listOfUsers[dniUserLogin] = user

    def closeSession(self):
        Persistence.saveData(self.listOfUsers, True, True, False)
        Persistence.saveFees(self.listOfFees, True)


    def getUser(self, dni: str, password: str,  admin: bool = False):
        user = self.listOfUsers.get(dni)
        if(user == None): return None
        else:
            if(user.verifyPassword(password) and not admin): return user
            elif(admin):
                if(user.isAdmin):  
                    if(user.verifyPassword(password)): return user
                else: return 'Not Admin'
            else: return None
            
    def exists(self, dni: str):
        user = self.listOfUsers.get(dni)
        if(user == None): return False
        return True

    def savePartner(self, user: User):
        d = date.today()
        if(d.month >= 6): price = 8
        else: price = 15
        self.listOfUsers[user.dni] =  user


        fees = self.listOfFees.get(str(d.year))

        if(self.listOfFees == None): self.listOfFees = {}

        if(fees != None): fees[user.dni] = Fee(d.year, str(d), True, price, 0)
        else: fees = { user.dni: Fee(d.year, str(d), True, price, 0) }
        
        self.listOfFees[str(d.year)] = fees

        Persistence.saveData(self.listOfUsers, True, True, False)
        Persistence.saveFees(self.listOfFees, True)

    def addFamily(self, dniOfPartner:str, dniOfFamily:str, type: str):

        partner = self.listOfUsers.get(dniOfPartner).partner
        familyPartner = self.listOfUsers.get(dniOfFamily).partner

        if(type=='parent'):
            if(partner.parents==None): partner.parents = [dniOfFamily]
            else: partner.parents.append(dniOfFamily)
        
            if(familyPartner.family==None): familyPartner.family = [dniOfPartner]
            else: familyPartner.family.append(dniOfPartner)

            self.updateDiscount(dniOfPartner, 15)
            self.updateDiscount(dniOfFamily, 15)

        elif(type=='children'):
            if(partner.childrens==None): partner.childrens = [dniOfFamily]
            else: partner.childrens.append(dniOfFamily)

            if(familyPartner.parents==None): familyPartner.parents = [dniOfPartner]
            else: familyPartner.family.append(dniOfPartner)

            self.updateDiscount(dniOfPartner, 15)
            self.updateDiscount(dniOfFamily, 15)

        elif(type=='couple'):
            partner.couple = dniOfFamily
            familyPartner.couple = dniOfPartner

            self.updateDiscount(dniOfPartner, 10)
            self.updateDiscount(dniOfFamily, 10)

        Persistence.saveData(self.listOfUsers, True, True, False)
        Persistence.saveFees(self.listOfFees, True)

    def updateDiscount(self, dni: str, discount: float):
        yearInfo = self.listOfFees.get(str(date.today().year))
        partnerInfo = yearInfo.get(dni)
        newDiscount = partnerInfo.discount + discount

        if(newDiscount>=25): partnerInfo.discount = 30
        #Actulizar a sus familiares
        else: partnerInfo.discount = newDiscount

        self.listOfFees[str(date.today().year)][dni] = partnerInfo 

    def searchFeesByYear(self, year: str):
        return [self.listOfFees.get(year), year]

    def updateFeesYearly(self):
        fees = self.listOfFees.get(str(date.today().year))

        if(fees != None): return True
        else:
            fees = self.listOfFees.get(str(date.today().year-1))
            self.listOfFees[str(date.today().year)] = fees
            Persistence.saveFees(self.listOfFees, True)
            return False
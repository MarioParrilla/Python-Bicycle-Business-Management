from src.model.Partner import *
from src.model.Fee import Fee
from src.core import Persistence
from datetime import date

class Club:

    def __init__(self, name: str, cif: str, socialBase: str):
        self.name = name
        self.cif = cif
        self.socialBase = socialBase
        self.listOfUsers = None
        self.listOfEvents = None
        self.totalBalance = 0
        self.listOfFees = None

    def init(self):
        data = Persistence.init()
        self.listOfUsers = data[0]
        self.listOfFees = data[1]

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


        fees = None

        if(self.listOfFees!=None): fees = self.listOfFees.get(user.dni)
        else: self.listOfFees = {}

        if(fees != None): fees[d.year] = Fee(d.year, str(d), True, price, 0)
        else: fees = { d.year: Fee(d.year, str(d), True, price, 0) }
        
        self.listOfFees[user.dni] = fees

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

        elif(type=='children'):
            if(partner.childrens==None): partner.childrens = [dniOfFamily]
            else: partner.childrens.append(dniOfFamily)

            if(familyPartner.parents==None): familyPartner.parents = [dniOfPartner]
            else: familyPartner.family.append(dniOfPartner)

        elif(type=='couple'):
            partner.couple = dniOfFamily
            familyPartner.couple = dniOfPartner

        Persistence.saveData(self.listOfUsers, True, True, False)


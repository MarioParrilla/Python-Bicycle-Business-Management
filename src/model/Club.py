from src.model.Partner import *
from src.model.Fee import Fee
from src.model.Event import Event
from src.core import Persistence
from datetime import date, datetime
from src.core.Utils import getDate

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
        self.listOfUsers, self.listOfFees, self.listOfEvents = Persistence.init()

    def closeSession(self, dniUserLogin: str):
        Persistence.saveData(self.listOfUsers, True, True)
        Persistence.saveFees(self.listOfFees, True)
        Persistence.saveEvents(self.listOfEvents)
        user = self.listOfUsers.get(dniUserLogin)
        user.lastAccess = str(datetime.today())
        self.listOfUsers[dniUserLogin] = user
        Persistence.saveData(self.listOfUsers, True, True)


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

        Persistence.saveData(self.listOfUsers, True, True)
        Persistence.saveFees(self.listOfFees, True)

    def checkEventsByUserDate(self, dni: str, date: str):
        if(self.listOfEvents == None): return True
        else:
            eventsOfDate = self.listOfEvents.get(date)

            if(eventsOfDate == None): return True
            else:
                for e in eventsOfDate:
                    if(e.date == date and e.organizer == dni):
                        return False

    #TODO: Esta funcion puede ser poco eficiente en la busquedaa REVISAR
    def getNearEvents(self):
        nearEvents = []

        now = datetime.today()
        if(not(self.listOfEvents == None)):
            for dateItems in self.listOfEvents.values():
                for e in dateItems:
                    d = getDate(e.date)
                    if(d >= now): nearEvents.append(e)

        return nearEvents

    def addUserToEvent(self, dni: str, event: Event):
            for date, lstEvents in self.listOfEvents.items():
                for e in lstEvents:
                    if(e==event):
                        if(e.eventPartners == None): e.eventPartners = [dni]
                        else: e.eventPartners.append(dni)
                        Persistence.saveEvents(self.listOfEvents)

    def saveEvent(self, event: Event):
        if(self.listOfEvents == None): self.listOfEvents = { event.date: [event] }
        else:
            l = self.listOfEvents.get(event.date)
            if(l == None): self.listOfEvents[event.date] = [event]
            else:
                l.append(event)
                self.listOfEvents[event.date] = l

        Persistence.saveEvents(self.listOfEvents)
    
    def getEventsByDate(self, date):
        dateEvents = []

        if(not(self.listOfEvents == None)):
            for dateItems in self.listOfEvents.values():
                for e in dateItems:
                    if(e.date== date): dateEvents.append(e)
        return dateEvents

    def getHistory(self, dni: str):
        history = []
        for year in self.listOfFees:
            for d in self.listOfFees.get(year):
                if(dni==d):
                    history.append(self.listOfFees.get(year).get(d))
                    break

        return history

    def addFamily(self, dniOfPartner:str, dniOfFamily:str, type: str):

        partner = self.listOfUsers.get(dniOfPartner).partner
        familyPartner = self.listOfUsers.get(dniOfFamily).partner

        if(type=='parent'):
            if(partner.parents==None): partner.parents = [dniOfFamily]
            else: partner.parents.append(dniOfFamily)
        
            if(familyPartner.parents==None): familyPartner.parents = [dniOfPartner]
            else: familyPartner.parents.append(dniOfPartner)

            self.updateDiscount(dniOfPartner, 15, True, False, False)

        elif(type=='children'):
            if(partner.childrens==None): partner.childrens = [dniOfFamily]
            else: partner.childrens.append(dniOfFamily)

            if(familyPartner.parents==None): familyPartner.parents = [dniOfPartner]
            else: familyPartner.family.append(dniOfPartner)

            self.updateDiscount(dniOfPartner, 15, False, True, False)

        elif(type=='couple'):
            partner.couple = dniOfFamily
            familyPartner.couple = dniOfPartner

            self.updateDiscount(dniOfPartner,  10, False, False, True)

        Persistence.saveData(self.listOfUsers, True, True)
        Persistence.saveFees(self.listOfFees, True)

    def updateDiscount(self, dni: str, discount: float, p: bool, ch: bool, c: bool):
        user = self.listOfUsers.get(dni).partner
        yearInfo = self.listOfFees.get(str(date.today().year))

        partnerInfo = yearInfo.get(dni)
        newDiscount = partnerInfo.discount + discount
        if(newDiscount>=25): 
            partnerInfo.discount = 30
            c = True
            ch = True
            
        else: partnerInfo.discount = newDiscount
        self.listOfFees[str(date.today().year)][dni] = partnerInfo 

        if(p):
            if(user.parents!=None):
                for i in user.parents:
                    parent = yearInfo.get(i)
                    parent.discount = parent.discount + discount
                    if(newDiscount>=25): parent.discount = 30
                    else: parent.discount = newDiscount
                    self.listOfFees[str(date.today().year)][i] = parent 

        if(ch):
            if(user.childrens!=None):
                for i in user.childrens:
                    children = yearInfo.get(i)
                    children.discount = children.discount + discount
                    if(newDiscount>=25): children.discount = 30
                    else: children.discount = newDiscount
                    self.listOfFees[str(date.today().year)][i] = children

        if(c):
            if(user.couple!=None):
                couple = yearInfo.get(user.couple)
                couple.discount = couple.discount + discount
                if(newDiscount>=25): couple.discount = 30
                else: couple.discount = newDiscount
                self.listOfFees[str(date.today().year)][user.couple] = couple

        

    def searchFeesByYear(self, year: str):
        return [self.listOfFees.get(year), year]

    def payFee(self, dni: str):
        self.updateFeesYearly()
        d = str(date.today().year)

        fee = self.listOfFees.get(d).get(dni)

        if(fee.isPaid): return None
        else:
            user = self.listOfUsers.get(dni)
            fee.year = d
            fee.isPaid = True
            newData = self.listOfFees.get(d)
            newData[dni] = fee
            self.listOfFees[d] = newData
            Persistence.saveFees(self.listOfFees, True)
            return [ user.partner.fullName, fee]

    def updateFeesYearly(self):
        fees = self.listOfFees.get(str(date.today().year))

        if(fees != None): return True
        else:
            fees = self.listOfFees.get(str(date.today().year-1))
            self.listOfFees[str(date.today().year)] = fees
            Persistence.saveFees(self.listOfFees, True)
            return False
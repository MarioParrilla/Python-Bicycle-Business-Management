from src.model.Partner import *
from src.model.Fee import Fee
from src.model.Event import Event
from src.model.Bike import Bike
from src.model.Maintenance import Maintenance
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

    def userCanJoin(self, dni: str):
        if(self.days_between(str(date.today()), self.listOfFees.get(str(date.today().year)).get(dni).lastPayment)>30): return False
        else: return True

    def days_between(self, d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)

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

    def getEventsOfUser(self, dni: str):
        data = []
        for date, lstEvents in self.listOfEvents.items():
            for e in lstEvents:
                if(not(e.eventPartners == None)):
                    if(not(e.eventPartners.index(dni) == None)): data.append(e)
        
        return data

    def addBikeToUser(self, user: User, bike: Bike):
        listBikesUser = user.partner.bikes
        if(listBikesUser == None): user.partner.bikes = [bike]
        else: user.partner.bikes.append(bike)
        self.listOfUsers[user.dni] = user
        Persistence.saveData(self.listOfUsers, True, True)

    def addMaintenaceToBike(self, dni: str, bike: Bike, maintenance: Maintenance):
        user = self.listOfUsers.get(dni)
        indexOfBike = user.partner.bikes.index(bike)
        b = user.partner.bikes[indexOfBike]
        if(b.maintenance==None): b.maintenance = [maintenance]
        else: b.maintenance.append(maintenance)
        user.partner.bikes[indexOfBike] = b
        self.listOfUsers[dni] = user
        Persistence.saveData(self.listOfUsers, True, True)

    def getMaintenances(self, dni: str):
        maintenances = []
        bikes = self.listOfUsers.get(dni).partner.bikes
        if(not(bikes == None)): maintenances = bikes

        return maintenances

    def getUserBikes(self, dni: str):
        user = self.listOfUsers.get(dni)
        return user.partner.bikes

    #TODO: Esta funcion puede ser poco eficiente en la busquedaa REVISAR
    def getNearEvents(self, type: str):
        nearEvents = []

        now = datetime.today()
        if(not(self.listOfEvents == None)):
            for dateItems in self.listOfEvents.values():
                for e in dateItems:
                    d = getDate(getattr(e, type))
                    if(d >= now): nearEvents.append(e)

        return nearEvents

    def addUserToEvent(self, dni: str, event: Event):
        
        for date, lstEvents in self.listOfEvents.items():
            for e in lstEvents:
                if(e==event):
                    if(e.eventPartners == None):
                        e.eventPartners = [dni]
                        return True
                    else: 
                        if(e.eventPartners.index(dni) == None):
                            e.eventPartners.append(dni)
                            Persistence.saveEvents(self.listOfEvents)
                            return True
                        else: return False

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

        success = False
        msg = ""

        partner = self.listOfUsers.get(dniOfPartner).partner
        familyPartner = self.listOfUsers.get(dniOfFamily).partner

        if(type=='parent'):
            cont = True
            if(partner.parents==None):
                if(partner.childrens!=None):
                    for c in partner.childrens:
                        if(c==dniOfFamily):
                            cont = False
                            break
                
                if(partner.couple!=None): 
                    if(partner.couple==dniOfFamily): cont = False

            elif(len(partner.parents)==2): cont = False
            else:
                for p in partner.parents:
                    if(p==dniOfFamily):
                        cont = False
                        break
                
                if(partner.childrens!=None):
                    for c in partner.childrens:
                        if(c==dniOfFamily):
                            cont = False
                            break
                
                if(partner.couple!=None): 
                    if(partner.couple==dniOfFamily): cont = False

            if(cont):
                if(partner.parents==None): partner.parents = [dniOfFamily]
                else: partner.parents.append(dniOfFamily)
            
                if(familyPartner.childrens==None): familyPartner.childrens = [dniOfPartner]
                else: familyPartner.childrens.append(dniOfPartner)

                self.updateDiscount(dniOfPartner, 15, True, False, False)
                success = True
            else:
                msg = f"No se ha permitido a??adir al socio {dniOfFamily} a los padres del socio {dniOfPartner}"
        
        elif(type=='children'):
            cont = True
            if(partner.childrens==None):
                if(partner.parents!=None):
                    for p in partner.parents:
                        if(p==dniOfFamily):
                            cont = False
                            break
                
                if(partner.couple!=None): 
                    if(partner.couple==dniOfFamily): cont = False
            else:
                if(partner.parents!=None):
                    for p in partner.parents:
                        if(p==dniOfFamily):
                            cont = False
                            break
                
                for c in partner.childrens:
                    if(p==dniOfFamily):
                        cont = False
                        break
                
                if(partner.couple!=None): 
                    if(partner.couple==dniOfFamily): cont = False

            if(cont):
                if(partner.childrens==None): partner.childrens = [dniOfFamily]
                else: partner.childrens.append(dniOfFamily)

                if(familyPartner.parents==None): familyPartner.parents = [dniOfPartner]
                else: familyPartner.family.append(dniOfPartner)

                self.updateDiscount(dniOfPartner, 15, False, True, False)
                success = True
            else:  msg = f"No se ha permitido a??adir al socio {dniOfFamily} como hijo del socio {dniOfPartner}"

        elif(type=='couple'):
            if(partner.couple == None and familyPartner.couple==None):
                if(partner.childrens==None and partner.parents==None):
                    partner.couple = dniOfFamily
                    familyPartner.couple = dniOfPartner

                    self.updateDiscount(dniOfPartner,  10, False, False, True)
                    success = True
                else:
                    cont = True
                    if(partner.parents!=None):
                        for p in partner.parents:
                            if(p==dniOfFamily):
                                msg = f"No se ha permitido a??adir al socio {dniOfFamily} como pareja del socio {dniOfPartner}"
                                cont = False
                                break
                    
                    if(partner.childrens!=None):
                        for c in partner.childrens:
                            if(c==dniOfFamily):
                                msg = f"No se ha permitido a??adir al socio {dniOfFamily} como pareja del socio {dniOfPartner}"
                                cont = False
                                break
                    
                if(cont):
                    partner.couple = dniOfFamily
                    familyPartner.couple = dniOfPartner

                    self.updateDiscount(dniOfPartner,  10, False, False, True)
                    success = True
            else:
                msg = f"No se ha permitido a??adir al socio {dniOfFamily} como pareja del socio {dniOfPartner}"
        
        Persistence.saveData(self.listOfUsers, True, True)
        Persistence.saveFees(self.listOfFees, True)

        if(success): return None
        else: return msg

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
                childrensPartner = user.childrens 
                childrensCouple = user.childrens 
                couple.discount = couple.discount + discount
                if(newDiscount>=25): couple.discount = 30
                else: couple.discount = newDiscount

                if(childrensPartner!=None):
                    for chn in childrensPartner:
                        cc = yearInfo.get(chn)
                        cc.discount = 30
                        self.listOfFees[str(date.today().year)][chn] = cc
    
                if(childrensPartner!=None):
                    for chn in childrensCouple:
                        cc = yearInfo.get(chn)
                        cc.discount = 30
                        self.listOfFees[str(date.today().year)][chn] = cc

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

            for dni, fee in fees.items():
                fee.isPaid = False
                fee.year = str(date.today().year)
                fees[dni] = fee

            self.listOfFees[str(date.today().year)] = fees
            Persistence.saveFees(self.listOfFees, True)
            return False
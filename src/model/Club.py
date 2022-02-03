from src.model.Partner import *
from src.core import Persistence
class Club:

    def __init__(self, name: str, cif: str, socialBase: str):
        self.name = name
        self.cif = cif
        self.socialBase = socialBase
        self.listOfUsers = None
        self.listOfEvents = None
        self.totalBalance = 0

    def init(self):
        self.listOfUsers = Persistence.init()

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
        self.listOfUsers[user.dni] =  user
        Persistence.saveData(self.listOfUsers, True, True, False)

    def addFamily(self, dniOfPartner:str, dniOfFamily:str, type: str):

        partner = self.listOfUsers.get(dniOfPartner).partner
        familyPartner = self.listOfUsers.get(dniOfFamily).partner

        if(type=='family'):
            if(partner.family==None): partner.family = [dniOfFamily]
            else: partner.family.append(dniOfFamily)
        
            if(familyPartner.family==None): familyPartner.family = [dniOfPartner]
            else: familyPartner.family.append(dniOfPartner)

        elif(type=='children'):
            if(partner.childrens==None): partner.childrens = [dniOfFamily]
            else: partner.childrens.append(dniOfFamily)

            if(familyPartner.family==None): familyPartner.family = [dniOfPartner]
            else: familyPartner.family.append(dniOfPartner)

        elif(type=='couple'):
            partner.couple = dniOfFamily
            familyPartner.couple = dniOfPartner

        Persistence.saveData(self.listOfUsers, True, True, False)


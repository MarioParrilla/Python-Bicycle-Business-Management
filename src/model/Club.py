from src.model.Partner import *
from src.core import Persistence
class Club:

    def __init__(self, name: str, cif: str, socialBase: str):
        self._name = name
        self._cif = cif
        self._socialBase = socialBase
        self._listOfPartners = None
        self._listOfEvents = None
        self._totalBalance = 0

    def init(self):
        self._listOfPartners = Persistence.init()

    def getUser(self, dni: str, password: str,  admin: bool = False):
        user = self._listOfPartners.get(dni)
        if(user == None): return None
        else:
            if(user.verifyPassword(password) and not admin): return user
            elif(admin):
                if(user._isAdmin):  
                    if(user.verifyPassword(password)): return user
                else: return 'Not Admin'
            else: return None
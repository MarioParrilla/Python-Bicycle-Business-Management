from src.model.Partner import *
from src.core import Persistence
class Club:

    def __init__(self, name: str, cif: str, socialBase: str):
        self.name = name
        self.cif = cif
        self.socialBase = socialBase
        self.listOfPartners = None
        self.listOfEvents = None
        self.totalBalance = 0

    def init(self):
        Persistence.init()
        self.listOfPartners = {'00000000A' : Partner('admin', 'c/admin', '000000000', 'a@a.com', '00000000A', 'admin', True)}

    def getUser(self, dni: str, password: str):
        user = self.listOfPartners.get(dni)
        if(user == None): return None
        else:
            if(user._user.verifyPassword(password)): return user._user
            else: return None
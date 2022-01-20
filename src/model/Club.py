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
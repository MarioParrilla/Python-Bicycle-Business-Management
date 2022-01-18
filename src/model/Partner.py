from src.model.Bicyclette import Bicyclette
#from src.model.User import User

class Partner:
    def __init__(self, user, fullName: str, address: str, phonenumber: str, email: str, 
                bicyclettes: list, family: list, childrens: list, couple = None):
        self.user = user
        self.fullName = fullName
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.bicyclettes = bicyclettes
        self.family = family
        self.childrens = childrens
        self.couple = couple
from model import User, Partner, Bicyclette

class Partner:
    def __init__(self, user: User, fullName: str, address: str, phonenumber: str, email: str, 
                bicyclettes: list, family: list, childrens: list, couple: Partner = None):
        self.user = user
        self.fullName = fullName
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.bicyclettes = bicyclettes
        self.family = family
        self.childrens = childrens
        self.couple = couple
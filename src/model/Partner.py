from src.model.Bicyclette import Bicyclette

class Partner:
    def __init__(self, fullName: str, address: str, phonenumber: str, email: str, dni: str, password: str, isAdmin: bool):
        self.fullName = fullName
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.bicyclettes = None
        self.family = None
        self.childrens = None
        self.couple = None
        self.user = User(dni, password, isAdmin, self)

from src.model.User import User
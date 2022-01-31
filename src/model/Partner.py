import hashlib

from src.model.Bicyclette import Bicyclette
from src.core.Utils import checkRegex


class Partner:
    def __init__(self, fullName: str, address: str, phonenumber: str, email: str):
        self.fullName = fullName
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.bikes = None
        self.family = None
        self.childrens = None
        self.couple = None

    def parseToJSON(self): 
        jsonObject = {
            'fullName': self.fullName,
            'address': self.address,
            'phonenumber': self.phonenumber,
            'email': self.email,
            'bikes': self.bikes,
            'family': self.family,
            'childrens': self.childrens,
            'couple': self.couple,
        }
        return jsonObject

class User:

    def __init__(self, fullName: str, address: str, phonenumber: str, email: str, dni: str, password: str, isAdmin: bool):
        self.dni = dni
        self.password = password
        self.lastAccess = '00/00/00 - 00:00:00'
        self.paid = True
        self.isAdmin = isAdmin
        self.partner = Partner(fullName, address, phonenumber, email)

    def __str__(self):
        return f"Socio: {self.partner.fullName}\nDNI: {self.dni}\nEmail: {self.partner.email}\nTelefono: {self.partner.phonenumber}"

    def parseToJSON(self): 
        jsonObject = {
            'dni': self.dni,
            'password': self.password,
            'lastAccess': self.lastAccess,
            'isAdmin': self.isAdmin,
            'paid': self.paid,
        }
        return jsonObject

    def encryptPassword(self):
        encrytedPass = hashlib.sha1(bytes(self.password, 'utf-8'))
        self.password = encrytedPass.hexdigest()

    def verifyPassword(self, password: str):
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        return self.password == encrytedPass.hexdigest()
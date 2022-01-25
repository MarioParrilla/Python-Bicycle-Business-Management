import hashlib

from src.model.Bicyclette import Bicyclette


class Partner:
    def __init__(self, fullName: str, address: str, phonenumber: str, email: str):
        self._fullName = fullName
        self._address = address
        self._phonenumber = phonenumber
        self._email = email
        self._bicyclettes = None
        self._family = None
        self._childrens = None
        self._couple = None

    def parseToJSON(self): 
        jsonObject = {
            'fullName': self._fullName,
            'address': self._address,
            'phonenumber': self._phonenumber,
            'email': self._email,
            'bicyclettes': self._bicyclettes,
            'family': self._family,
            'childrens': self._childrens,
            'couple': self._couple,
        }
        return jsonObject
class User:

    def __init__(self, fullName: str, address: str, phonenumber: str, email: str, dni: str, password: str, isAdmin: bool):
        self._dni = dni
        self._password = password
        self._lastAccess = '00/00/00 - 00:00:00'
        self._paid = True
        self._isAdmin = isAdmin
        self._partner = Partner(fullName, address, phonenumber, email)

    def parseToJSON(self): 
        jsonObject = {
            'dni': self._dni,
            'password': self._password,
            'lastAccess': self._lastAccess,
            'isAdmin': self._isAdmin,
            'paid': self._paid,
        }
        return jsonObject

    def encryptPassword(self):
        encrytedPass = hashlib.sha1(bytes(self._password, 'utf-8'))
        self._password = encrytedPass.hexdigest()

    def verifyPassword(self, password: str):
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        return self._password == encrytedPass.hexdigest()

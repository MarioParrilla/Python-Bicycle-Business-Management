import hashlib
from src.model.Bicyclette import Bicyclette

class Partner:
    def __init__(self, fullName: str, address: str, phonenumber: str, email: str, dni: str, password: str, isAdmin: bool):
        self._fullName = fullName
        self._address = address
        self._phonenumber = phonenumber
        self._email = email
        self._bicyclettes = None
        self._family = None
        self._childrens = None
        self._couple = None
        self._user = User(dni, password, isAdmin, self)

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
            'User':{
                'dni': self._user._dni,
                'password': self._user._password,
                'lastAccess': self._user._lastAccess,
                'lastAccess': self._user._lastAccess,
                'isAdmin': self._user._isAdmin
            }
        }

        return jsonObject

class User:

    def __init__(self, dni: str, password: str, isAdmin: bool, partner: Partner):
        self._dni = dni
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        self._password = encrytedPass.hexdigest()
        self._lastAccess = None
        self._isAdmin = isAdmin
        self._partner = partner

    def verifyPassword(self, password: str):
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        return self.password == encrytedPass.hexdigest()
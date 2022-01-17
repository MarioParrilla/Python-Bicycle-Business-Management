import hashlib
from model import Partner

class User:

    def __init__(self, dni: str, password: str, lastAccess: str, isAdmin: bool, partner: Partner):
        self.dni = dni
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        self.password = encrytedPass.hexdigest()
        self.lastAccess = lastAccess
        self.isAdmin = isAdmin
        self.partner = partner

    def verifyPassword(self, password: str):
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        return self.password == encrytedPass.hexdigest()
    
    
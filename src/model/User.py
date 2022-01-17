import hashlib

class User:

    def __init__(self, dni: str, password: str, lastAccess: str, isAdmin: bool):
        self.dni = dni
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        self.password = encrytedPass.hexdigest()
        self.lastAccess = lastAccess
        self.isAdmin = isAdmin

    def verifyPassword(self, password: str):
        encrytedPass = hashlib.sha1(bytes(password, 'utf-8'))
        return self.password == encrytedPass.hexdigest()
    
    
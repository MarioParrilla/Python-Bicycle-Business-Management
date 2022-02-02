import json, os
from src.model.Partner import *

PATHUSER = './src/data/users.json'
PATHPARTNER = './src/data/partners.json'

def init():
    createUsersFile = False
    createPartnersFile = False 

    if(not(os.path.exists(PATHUSER))): createUsersFile = True
    if(not(os.path.exists(PATHPARTNER))): createPartnersFile = True

    if(createUsersFile or createPartnersFile): saveData({'00000000A' : User('admin', 'c/admin', '000000000', 'a@a.com', '00000000A', 'admin', True)}, createUsersFile, createPartnersFile, True)
    return _readDefault()

#Se comrpueba si existen los ficheros por defecto y si no existen se crean con lo datos por defecto
def saveData(listOfPartners: list, createUsersFile: bool, createPartnersFile: bool, encrypt: bool): 
    listUsers = []
    listPartners = []
    for i in listOfPartners:
        user = listOfPartners.get(i)
        if(encrypt): user.encryptPassword()
        if(createUsersFile): listUsers.append(user.parseToJSON())

        if(createPartnersFile): listPartners.append(user.partner.parseToJSON())

    if(createUsersFile):
        file = open(PATHUSER,'w')
        json.dump(listUsers, file, indent=4)
        file.close()

    if(createPartnersFile):
        file = open(PATHPARTNER, 'w')
        json.dump(listPartners, file, indent=4)
        file.close()

#Se leen llos ficheros para cargar los datos ya existentes y se relacionan cada usuario con su socio
def _readDefault():
    listUsers = {}

    file = open(PATHPARTNER)
    partners = json.load(file)

    file = open(PATHUSER)
    users = json.load(file)

    for i in range(len(partners)):
        partner = partners[i]
        user = users[i]
        listUsers[user['dni']] = User(partner['fullName'], partner['address'], partner['phonenumber'], partner['email'], user['dni'], user['password'], user['isAdmin'])

    return listUsers
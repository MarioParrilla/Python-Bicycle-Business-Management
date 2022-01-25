import json, os
from src.model.Partner import *

PATHUSER = './src/data/users.json'
PATHPARTNER = './src/data/partners.json'

def init():
    createUsersFile = False
    createPartnersFile = False 

    if(not(os.path.exists(PATHUSER))): createUsersFile = True
    if(not(os.path.exists(PATHPARTNER))): createPartnersFile = True

    if(createUsersFile or createPartnersFile): _writeDefault({'00000000A' : User('admin', 'c/admin', '000000000', 'a@a.com', '00000000A', 'admin', True)}, createUsersFile, createPartnersFile)
    return _readDefault()

def _writeDefault(listOfPartners: list, createUsersFile: bool, createPartnersFile: bool): 
    listUsers = []
    listPartners = []
    for i in listOfPartners:
        user = listOfPartners.get(i)
        user.encrytedPass()
        if(createUsersFile): listUsers.append(user.parseToJSON())

        if(createPartnersFile): listPartners.append(user._partner.parseToJSON())

    if(createUsersFile):
        file = open(PATHUSER, 'a')
        json.dump(json.dumps(listUsers), file)
        file.close()

    if(createPartnersFile):
        file = open(PATHPARTNER, 'a')
        json.dump(json.dumps(listPartners), file)
        file.close()

def _readDefault():
    listUsers = {}

    file = open(PATHPARTNER)
    partners = json.loads(json.load(file))

    file = open(PATHUSER)
    users = json.loads(json.load(file))

    for i in range(len(partners)):
        partner = partners[i]
        user = users[i]
        listUsers[user['dni']] = User(partner['fullName'], partner['address'], partner['phonenumber'], partner['email'], user['dni'], user['password'], user['isAdmin'])

    return listUsers
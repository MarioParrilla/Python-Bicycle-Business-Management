import json, os
from src.model.Partner import *
from src.model.Fee import Fee
from datetime import date

PATHUSER = './src/data/users.json'
PATHPARTNER = './src/data/partners.json'
PATHFEES = './src/data/fees.json'

def init():
    createUsersFile = False
    createPartnersFile = False 

    if(not(os.path.exists(PATHUSER))): createUsersFile = True
    if(not(os.path.exists(PATHPARTNER))): createPartnersFile = True

    if(createUsersFile or createPartnersFile): saveData({'00000000A' : User('admin', 'c/admin', '000000000', 'a@a.com', '00000000A', 'admin', True)}, createUsersFile, createPartnersFile, True)
    saveFees({ '00000000A': { date.today().year: Fee(date.today().year, str(date.today()), True, 0, 0) } }, True)
    return _readDefault()

#Se comrpueba si existen los ficheros por defecto y si no existen se crean con lo datos por defecto
def saveData(listOfPartners: dict, createUsersFile: bool, createPartnersFile: bool, encrypt: bool): 
    listUsers = []
    listPartners = []
    for i in listOfPartners:
        user = listOfPartners.get(i)
        
        if(createUsersFile): 
            if(encrypt): user.encryptPassword()
            listUsers.append(user.parseToJSON())

        if(createPartnersFile): listPartners.append(user.partner.parseToJSON())

    if(createUsersFile):
        file = open(PATHUSER,'w')
        json.dump(listUsers, file, indent=4)
        file.close()

    if(createPartnersFile):
        file = open(PATHPARTNER, 'w')
        json.dump(listPartners, file, indent=4)
        file.close()

def saveFees(fees: dict, createFeesFile):
    if(createFeesFile):
        dictOfFees = {}
        file = open(PATHFEES, 'w')

        for dni in fees:
            years = {}
            for year in fees.get(dni):
                years[year] =  fees.get(dni).get(year).parseToJSON()

            dictOfFees[dni] = years

        json.dump(dictOfFees, file, indent=4)
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

        object = User(partner['fullName'], partner['address'], partner['phonenumber'], partner['email'], user['dni'], user['password'], user['isAdmin'])

        object.partner.parents = partner['parents']
        object.partner.childrens = partner['childrens']
        object.partner.couple = partner['couple']

        listUsers[object.dni] = object
        

    return listUsers
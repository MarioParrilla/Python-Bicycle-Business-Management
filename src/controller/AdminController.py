from src.model.Club import Club
from src.model.Partner import *
from src.view.View import printMessage
from src.view.AdminView import View
class AdminController:

    def __init__(self, club: Club, dni: str, password: str):
        self.club = club
        self.club.init()
        userChecked = self.club.getUser(dni, password, True)
        if(isinstance(userChecked, User)): 
            self.user = userChecked
            self.run = True
        elif(userChecked=='Not Admin'): 
            self.run = False
            printMessage('❗Error en el login: El usuario no es administrator.', 'red')
        else:
            self.run = False
            printMessage('❗Error en el login: Usuario incorrecto o Contraseña incorrecta.', 'red')
        self.view = View(self)
    
    def init(self):
        while self.run:
            selection = self.view.menu(self.club.name, self.user.dni, self.user.lastAccess)
            if( selection   == '0' or selection == 'exit' ): 
                self.club.closeSession(self.user.dni)
                self.run = False
            elif( selection == '1' ): self.view.showInfoPartners(self.club.listOfUsers)
            elif( selection == '2' ): self.view.requestNewPartner()
            elif( selection == '3' ): self.view.addFamilyToPartner()
            elif( selection == '4' ): self.view.showNearEvents(self.club.getNearEvents())
            elif( selection == '5' ): pass
            elif( selection == '6' ): 
                data = None
                while(True):
                    data = self.view.requestInfoEvent()
                    if(not(data == False)): break
                self.club.saveEvent(data)
            elif( selection == '7' ): self.view.showFeesByYear(self.club.searchFeesByYear(self.view.feeByYear()))
            elif( selection == '8' ): self.view.warnUpdateFees(self.club.updateFeesYearly())
            elif( selection == '9' ): self.view.showDataPay(self.club.payFee(self.view.requestDni()))
            else: printMessage(f'❗No existe la opcion {selection}', 'red')

    def existDni(self, dni:str):
        return self.club.exists(dni)

    def addFamiliy(self, dniOfPartner:str, dniOfFamily:str, type: str):
        self.club.addFamily(dniOfPartner, dniOfFamily, type)

    def saveNewPartner(self, user: User):
        self.club.savePartner(user)

    def checkEventsByUserDate(self, dni: str, date: str):
        return self.club.checkEventsByUserDate(dni, date)
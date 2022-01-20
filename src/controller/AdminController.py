from src.model.Club import Club
from src.model.Partner import *
from src.view.View import printMessage
from src.view.AdminView import AdminView

class AdminController:

    def __init__(self, club: Club, dni: str, password: str):
        self.club = club
        self.club.init()
        userChecked = club.getUser(dni, password)
        if(userChecked!=None): 
            self.user = userChecked
            self.run = True
        else:
            self.run = False
            printMessage('❗Error en el login: Usuario incorrecto o Contraseña incorrecta.', 'red')
        self.view = AdminView()
    
    def init(self):
        while self.run:
            selection = self.view.menu(self.club.name, 'usuarioPrueba', '00/00/00 - 00:00:00')
            if( selection   == '0' or selection == 'exit' ): self.run = False
            elif( selection == '1' ): pass
            elif( selection == '2' ): pass
            elif( selection == '3' ): pass
            elif( selection == '4' ): pass
            elif( selection == '5' ): pass
            elif( selection == '6' ): pass
            elif( selection == '7' ): pass
            elif( selection == '8' ): pass
            elif( selection == '9' ): pass
            else: View.printMessage(f'❗No existe la opcion {selection}', 'red')
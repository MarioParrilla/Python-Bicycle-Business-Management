from src.model.Club import Club
from src.model.Partner import *
from src.view.View import printMessage
from src.view.AdminView import AdminView

class AdminController:

    def __init__(self, club: Club, dni: str, password: str):
        self._club = club
        self._club.init()
        userChecked = self._club.getUser(dni, password, True)
        if(isinstance(userChecked, User)): 
            self._user = userChecked
            self._run = True
        elif(userChecked=='Not Admin'): 
            self._run = False
            printMessage('❗Error en el login: El usuario no es administrator.', 'red')
        else:
            self._run = False
            printMessage('❗Error en el login: Usuario incorrecto o Contraseña incorrecta.', 'red')
        self._view = AdminView()
    
    def init(self):
        while self._run:
            selection = self._view.menu(self._club._name, self._user._dni, self._user._lastAccess)
            if( selection   == '0' or selection == 'exit' ): self._run = False
            elif( selection == '1' ): pass
            elif( selection == '2' ): pass
            elif( selection == '3' ): pass
            elif( selection == '4' ): pass
            elif( selection == '5' ): pass
            elif( selection == '6' ): pass
            elif( selection == '7' ): pass
            elif( selection == '8' ): pass
            elif( selection == '9' ): pass
            else: printMessage(f'❗No existe la opcion {selection}', 'red')
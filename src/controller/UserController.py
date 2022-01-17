from src.model import Club
from src.view.View import View
from src.view.UserView import UserView

class UserController:

    def __init__(self, club: Club, dni: str, password: str):
        self.club = club
        self.dni = dni
        self.password = password
        self.view = UserView()

    def init(self):
        while True:
            selection = self.view.menu()
            if( selection   == '0' or selection == 'exit' ): break
            elif( selection == '1' ): pass
            elif( selection == '2' ): pass
            elif( selection == '3' ): pass
            elif( selection == '4' ): pass
            elif( selection == '5' ): pass
            elif( selection == '6' ): pass
            elif( selection == '7' ): pass
            elif( selection == '8' ): pass
            else: View.printMessage(f'❗No existe la opcion {selection}', 'red')
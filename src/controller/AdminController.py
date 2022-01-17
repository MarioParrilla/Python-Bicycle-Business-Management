from src.model import Club
from view import AdminView, View

class AdminController:

    def __init__(self, club: Club):
        self.club = club
        self.view = AdminView()
    
    def init(self):
        while True:
            selection = self.view.Menu()
            if( selection   == '0' or selection == 'exit' ): break
            elif( selection == '1' ): pass
            elif( selection == '2' ): pass
            elif( selection == '3' ): pass
            elif( selection == '4' ): pass
            elif( selection == '5' ): pass
            elif( selection == '6' ): pass
            elif( selection == '7' ): pass
            elif( selection == '8' ): pass
            elif( selection == '9' ): pass
            else: View.printMessage(f'❗No existe la opcion {selection}')
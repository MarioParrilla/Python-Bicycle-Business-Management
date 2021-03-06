from src.model import Club
from src.view.View import printMessage
from src.view.UserView import UserView
from src.model.Event import Event
from src.model.Bike import Bike
from src.model.Maintenance import Maintenance

class UserController:

    def __init__(self, club: Club, dni: str, password: str):
        self.club = club
        self.club.init()
        userChecked = club.getUser(dni, password)
        if(userChecked!=None and self.club.userCanJoin(userChecked.dni)): 
            self.user = userChecked
            self.run = True
        elif(not(self.club.userCanJoin(userChecked.dni))):
            self.run = False
            printMessage('❗Error en el login: El usuario no ha pagado en 30 dias.', 'red')
        else:
            self.run = False
            printMessage('❗Error en el login: Usuario incorrecto o Contraseña incorrecta.', 'red')
        self.view = UserView(self)

    def init(self):
        while self.run:
            selection = self.view.menu(self.club.name, self.user.dni, self.user.lastAccess)
            if( selection   == '0' or selection == 'exit' ): 
                self.club.closeSession(self.user.dni)
                self.run = False
            elif( selection == '1' ): self.view.showEventsOfUser(self.club.getEventsOfUser(self.user.dni))
            elif( selection == '2' ): self.view.joinToEvents(self.user.dni, self.club.getNearEvents('maxDate'))
            elif( selection == '3' ): self.view.showBikesOfUser(self.club.getUserBikes(self.user.dni))
            elif( selection == '4' ): self.view.showMaintenances(self.club.getMaintenances(self.user.dni))
            elif( selection == '5' ): self.club.addBikeToUser(self.user, self.view.requestInfoBikes())
            elif( selection == '6' ): self.view.addMaintenaceToBike(self.user.dni, self.club.getUserBikes(self.user.dni))
            elif( selection == '7' ): self.view.showFamily([self.user.partner.parents, self.user.partner.childrens, self.user.partner.couple])
            elif( selection == '8' ): self.view.showHistory(self.club.getHistory(self.user.dni))
            else: printMessage(f'❗No existe la opcion {selection}', 'red')
    
    def addUserToEvent(self, dni: str, event: Event):
        return self.club.addUserToEvent(dni, event)
    
    def addMaintenaceToBike(self, dni: str, bike: Bike, maintenance: Maintenance):
        self.club.addMaintenaceToBike(dni, bike, maintenance)

    
from src.view.View import View

class UserView:

    def __init__(self):
        pass

    def menu(self, clubName, userName, lastAccess):
        View.screen(clubName, userName, lastAccess)
        View.printMessage('Menu');
        View.printMessage('====');
        View.printMessage('1. Ver mis próximos eventos y la lista de inscritos.');
        View.printMessage('2. Ver y apuntarme a eventos abiertos.');
        View.printMessage('3. Ver mis bicicletas.');
        View.printMessage('4. Ver mis reparaciones/mantenimientos.');
        View.printMessage('5. Añadir nueva bicicleta.');
        View.printMessage('6. Añadir reparación/mantenimiento a una de mis bicicletas.');
        View.printMessage('7. Ver mi familia.');
        View.printMessage('8. Ver mi histórico y estado de cuotas con toda su información.');
        View.printMessage('0. Salir.');
        print(">>> ", end = '')
        return input()

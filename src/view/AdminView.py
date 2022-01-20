from src.core.Utils import clear
from src.view.View import printMessage, screen
class AdminView:

    def __init__(self):
        pass

    def menu(self, clubName, userName, lastAccess):
        clear()
        screen(clubName, userName, lastAccess, True)
        printMessage('Menu')
        printMessage('====')
        printMessage('1. Ver listado completo de socios.')
        printMessage('2. Insertar un nuevo socio.')
        printMessage('3. Añadir a un socio su familia.')
        printMessage('4. Ver listado completo de los próximos eventos.')
        printMessage('5. Buscar eventos por fecha y mostrar toda su información.')
        printMessage('6. Insertar un nuevo evento.')
        printMessage('7. Ver el control de cuotas-socios por años.')
        printMessage('8. Actualizar el control de cuotas-socio para el año en curso.')
        printMessage('9. Realizar el pago de una cuota por DNI de socio.')
        printMessage('0. Salir.')
        print(">>> ", end = '')
        return input()

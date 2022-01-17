from src.view.View import View

class AdminView:

    def __init__(self):
        pass

    def menu(self):
        View.printMessage('1. Ver listado completo de socios.');
        View.printMessage('2. Insertar un nuevo socio.');
        View.printMessage('3. Añadir a un socio su familia.');
        View.printMessage('4. Ver listado completo de los próximos eventos.');
        View.printMessage('5. Buscar eventos por fecha y mostrar toda su información.');
        View.printMessage('6. Insertar un nuevo evento.');
        View.printMessage('7. Ver el control de cuotas-socios por años.');
        View.printMessage('8. Actualizar el control de cuotas-socio para el año en curso.');
        View.printMessage('9. Realizar el pago de una cuota por DNI de socio.');
        View.printMessage('0. Salir.');

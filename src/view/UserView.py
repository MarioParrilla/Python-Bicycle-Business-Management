from src.view.View import printMessage, screen, pause
from src.core.Utils import checkRegex, getDate
from src.model.Bike import Bike
class UserView:

    def __init__(self, controller):
        self.controller = controller

    def menu(self, clubName, userName, lastAccess):
        screen(clubName, userName, lastAccess)
        printMessage('Menu');
        printMessage('====');
        printMessage('1. Ver mis próximos eventos y la lista de inscritos.');
        printMessage('2. Ver y apuntarme a eventos abiertos.');
        printMessage('3. Ver mis bicicletas.');
        printMessage('4. Ver mis reparaciones/mantenimientos.');
        printMessage('5. Añadir nueva bicicleta.');
        printMessage('6. Añadir reparación/mantenimiento a una de mis bicicletas.');
        printMessage('7. Ver mi familia.');
        printMessage('8. Ver mi histórico y estado de cuotas con toda su información.');
        printMessage('0. Salir.');
        print(">>> ", end = '')
        return input()

    def requestInfoBikes(self):
        date = ''
        brandName = ''
        model = ''
        price = ''
        typeBike = ''
        color = ''
        bikeFrameSize = ''
        wheelSize = ''

        while(True):
            printMessage('Introduce la fecha de compra de la bicicleta:', 'yellow')
            print(">>> ", end = '')
            date = input()
            if(checkRegex(date, 'date')): break;
            else: printMessage('❗Introduce una fecha con el formato dia/mes/año')

        while(True):
            printMessage('Introduce la marca de la bicicleta:', 'yellow')
            print(">>> ", end = '')
            brandName = input()
            if(len(brandName.strip())>0): break;
            else: printMessage('❗Introduce una  marca')

        while(True):
            printMessage('Introduce el modelo de bicicleta:', 'yellow')
            print(">>> ", end = '')
            model = input()
            if(len(model.strip())>0): break;
            else: printMessage('❗Introduce un modelo de bicicleta')
        
        while(True):
            printMessage('Introduce el precio de la bicicleta:', 'yellow')
            print(">>> ", end = '')
            if(len(price.strip())>=0): 
                try: 
                    price = input()
                    price = float(price)
                    break;
                except: printMessage('❗Introduce un precio valido')
            else: printMessage('❗Introduce un precio valido')

        while(True):
            printMessage('Introduce el tipo de bicicleta:', 'yellow')
            print(">>> ", end = '')
            typeBike = input()
            if(len(typeBike.strip())>0): break;
            else: printMessage('❗Introduce un tipo de bicicleta')

        while(True):
            printMessage('Introduce el color de la bicicleta:', 'yellow')
            print(">>> ", end = '')
            color = input()
            if(len(color.strip())>0): break;
            else: printMessage('❗Introduce el color de la bicicleta')
        
        while(True):
            printMessage('Introduce el tamaño del cuadro de la bicicleta:', 'yellow')
            print(">>> ", end = '')
            if(len(bikeFrameSize.strip())>=0):
                try: 
                    bikeFrameSize = input()
                    bikeFrameSize = float(bikeFrameSize)
                    break;
                except:  printMessage('❗Introduce el tamaño del cuadro de la bicicleta valido')
            else: printMessage('❗Introduce el tamaño del cuadro de la bicicleta valido')
        
        while(True):
            printMessage('Introduce el tamaño de rueda de la bicicleta:', 'yellow')
            print(">>> ", end = '')
            if(len(wheelSize.strip())>=0):
                try: 
                    wheelSize = input()
                    wheelSize = float(wheelSize)
                    break;
                except: printMessage('❗Introduce el tamaño de rueda de la bicicleta valido')
            else: printMessage('❗Introduce el tamaño de rueda de la bicicleta valido')

        return Bike(date, brandName, model, price, typeBike, color, bikeFrameSize, wheelSize)

    def showFamily(self, data: list):
        parents, children, couple = data

        if(parents != None):
            printMessage(f'Padres', 'yellow')
            for p in parents:
                printMessage(f'{p}\n')
        
        if(children != None): 
            printMessage(f'Hijos', 'yellow')
            for c in children:
                printMessage(f'{c}\n')

        if(couple != None): 
            printMessage(f'Pareja', 'yellow')
            printMessage(f'{couple}\n')
        pause()

    def showHistory(self, data: list):
        printMessage(f'Historico de Cuotas', 'cyan')
        printMessage(f'===================', 'cyan')
        for fee in data:
            printMessage(f'{fee}\n')
            pause()

    def showEventsOfUser(self, events: list):
        printMessage('\nLista de Eventos Inscritos', 'cyan')
        printMessage('============================')
        if(len(events) == 0): printMessage('Ninguno')
        else:
            for e in events:
                printMessage(f'{e}')
                pause()

    def joinToEvents(self, dni: str, events: list):
        printMessage('\nLista de Eventos Cernanos', 'cyan')
        printMessage('============================')
        if(len(events) == 0): printMessage('Ninguno')
        else:
            for e in events:
                printMessage(f'{e}')
                while(True):
                    printMessage('¿Quieres apuntarte? [Si/No]:', 'yellow')
                    print(">>> ", end = '')
                    isAdmin = input()
                    if(isAdmin.lower()=='si'):
                        if(self.controller.addUserToEvent(dni, e)): printMessage('Apuntado Correctamente en el evento', 'green')
                        else: printMessage('Ya esta apuntado a este evento', 'red')
                        break;
                    elif(isAdmin.lower()=='no'): break;
                    else: printMessage('❗Introduce un valor valido')
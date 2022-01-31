
from src.view.View import printMessage, screen
from src.core.Utils import checkRegex
class View:

    def __init__(self):
        pass

    def menu(self, clubName, userName, lastAccess):
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

    def showInfoPartners(self, listOfUser: dict):
        printMessage('\nLista de Socios', 'cyan')
        printMessage('===============')
        for user in listOfUser:
            printMessage(f'{listOfUser.get(user)}\n')

    def requestNewPartner(self):
        fullname = ''
        address = ''
        phonenumber = ''
        email = ''
        dni = ''
        password = ''
        isAdmin = ''

        #Request fullName
        while(True):
            printMessage('Introduce un nombre para el socio (Nombre y Apellidos):', 'yellow')
            print(">>> ", end = '')
            fullname = input()
            if(len(fullname.strip())>5): break;
            else: printMessage('❗Introduce un nombre y apellidos mayor a 5 digitos')
        
        #Request Address
        while(True):
            printMessage('Introduce una direccion de calle:', 'yellow')
            print(">>> ", end = '')
            address = input()
            if(len(address.strip())>0): break;
            else: printMessage('❗Introduce una direccion')

        #Request Address
        while(True):
            printMessage('Introduce un numero de telefono:', 'yellow')
            print(">>> ", end = '')
            phonenumber = input()
            if(checkRegex(phonenumber, 'phonenumber')): break;
            else: printMessage('❗Introduce un telefono valido')

        #Request email
        while(True):
            printMessage('Introduce un email:', 'yellow')
            print(">>> ", end = '')
            email = input()
            if(checkRegex(email, 'email')): break;
            else: printMessage('❗Introduce un email valido')

        #Request DNI
        while(True):
            printMessage('Introduce un dni:', 'yellow')
            print(">>> ", end = '')
            dni = input()
            if(checkRegex(dni, 'dni')): break;
            else: printMessage('❗Introduce un dni valido')

        #Request Password
        while(True):
            printMessage('Introduce una contraseña:', 'yellow')
            print(">>> ", end = '')
            password = input()
            if(len(password.strip())>5): break;
            else: printMessage('❗Introduce una contraseña mayor a 5 digitos')


        #Request isAdmin
        while(True):
            printMessage('Introduce si es admin [Si/No]:', 'yellow')
            print(">>> ", end = '')
            isAdmin = input()
            if(isAdmin.lower()=='si'):
                isAdmin = True
                break;
            elif(isAdmin.lower()=='no'):
                isAdmin = False
                break;
            else: printMessage('❗Introduce un valor valido')
        
        print(f'{fullName}, {address}, {phonenumber}, {email}, {password}, {isAdmin}')
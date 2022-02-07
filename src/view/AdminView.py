
from src.view.View import printMessage, screen
from src.core.Utils import checkRegex
from src.model.Partner import User
from datetime import date
class View:

    def __init__(self, controller):
        self.controller = controller

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
        for user in sorted(listOfUser.items(), key=lambda x: x[1].partner.fullName):
            printMessage(f'{listOfUser.get(user[0])}\n')

    def addFamilyToPartner(self):
        partnerDni = None
        while True:
            printMessage('\nIntroduce el dni del socio: ')
            print(">>> ", end = '')
            partnerDni = input()
            if(self.controller.existDni(partnerDni)): break;
            else: printMessage('❗Introduce un dni valido')

        run = True
        while(run):
            printMessage('\nIntroduce que tipo de familiar es: [Padre, Hijo, Pareja]', 'yellow')
            print(">>> ", end = '')
            type = input()
            if(type == 'padre' or type == 'hijo' or type == 'pareja'): run = self.addFamiliy(partnerDni, type)
            else: printMessage('❗Introduce un tipo de familiar valido')
                

    def warnUpdateFees(self, wasUpdated: bool):
        if(wasUpdated): printMessage('Ya esta actualizado el estado de las cuotas\n', 'cyan')
        else: printMessage('Actualizado el estado de las cuotas\n', 'green')

    def feeByYear(self):
        year = ''
        while True:
            printMessage('Introduce el año a mostrar: ', 'yellow')
            year = input()
            if(len(year.strip()) == 0): 
                year = str(date.today().year)
                break;
            elif(len(year.strip())>=4 and int(year)): break;
            else: printMessage('❗Introduce un año valido')
        return year

    def showFeesByYear(self, data: list):
        fees, year = data 
        if(fees!=None):
            printMessage(f'Cuotas Socios {year}', 'cyan')
            printMessage('=====================', 'cyan')
            for fee in sorted(fees.items(), key=lambda x: x[1].isPaid):
                printMessage(f'\n{fee[0]}:\n{fees.get(fee[0])}')
        else: printMessage(f'❗El año {year} no existe en los registros')

    def addFamiliy(self, partnerDni: str, type: str):
        target = ''
        if(type=='padre'): target = 'parent'
        elif(type=='hijo'): target = 'children'
        elif(type=='pareja'): target = 'couple'
        while(True):
            printMessage(f'Introduce un dni de {type}: ')
            print(">>> ", end = '')
            familyDni = input()
            
            if(partnerDni!=familyDni):
                if(self.controller.existDni(familyDni)): 
                    self.controller.addFamiliy(partnerDni, familyDni, target)
                    return False
                else: printMessage('❗Introduce un dni valido') 
            else: printMessage('❗Introduce un dni que no sea el mismo que el socio objetivo') 


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
            if(checkRegex(dni, 'dni')): 
                if(not(self.controller.existDni(dni))): break
                else: printMessage('❗Introduce un dni que no exista ya')
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
        
        self.controller.saveNewPartner(User(fullname, address, phonenumber, email, dni, password, isAdmin))

from src.view.View import printMessage, screen, pause
from src.core.Utils import checkRegex, getDate
from src.model.Partner import User
from src.model.Event import Event
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

    def showNearEvents(self, events: list):
        printMessage('\nLista de Eventos Cernanos', 'cyan')
        printMessage('============================')
        for e in events:
            printMessage(f'{e}')
            pause()

    def requestInfoEvent(self):
        date = ''
        organizer = ''
        maxDate = ''
        location = ''
        province = ''
        totalKM = 0
        price = 0

        while(True):
            printMessage('Introduce una fecha para el evento:', 'yellow')
            print(">>> ", end = '')
            date = input()
            if(checkRegex(date, 'date')): break;
            else: printMessage('❗Introduce una fecha con el formato dia/mes/año')

        while(True):
            printMessage('Introduce el dni del organizador:', 'yellow')
            print(">>> ", end = '')
            organizer = input()
            if(checkRegex(organizer, 'dni')): 
                if(self.controller.existDni(organizer)): 
                    if(self.controller.checkEventsByUserDate(organizer, date)): break
                    else: printMessage('❗Introduce una fecha donde este usuario no tenga ya un evento')
                else: printMessage('❗Introduce un dni que ya exista')
            else: printMessage('❗Introduce un dni valido')

        while(True):
            printMessage('Introduce una fecha de inscripcion:', 'yellow')
            print(">>> ", end = '')
            maxDate = input()
            if(checkRegex(maxDate, 'date')): 
                if(getDate(date)>getDate(maxDate)): break
                else: printMessage('❗Introduce una fecha de inscripcion que sea antes de la fecha del evento')
            else: printMessage('❗Introduce una fecha con el formato dia/mes/año')

        while(True):
            printMessage('Introduce una localidad:', 'yellow')
            print(">>> ", end = '')
            location = input()
            if(len(location.strip())>0): break;
            else: printMessage('❗Introduce una localidad')

        while(True):
            printMessage('Introduce una provincia:', 'yellow')
            print(">>> ", end = '')
            province = input()
            if(len(province.strip())>0): break;
            else: printMessage('❗Introduce una provincia')

        while(True):
            printMessage('Introduce el recorrido total en kilometros:', 'yellow')
            print(">>> ", end = '')
            totalKM = input()
            if(len(totalKM.strip())>0):
                try:
                    totalKM = float(totalKM.strip())
                    break
                except:
                    printMessage('❗Introduce un numero correcto')

            else: printMessage('❗Introduce un numero correcto')

        while(True):
            printMessage('Introduce el precio del evento:', 'yellow')
            print(">>> ", end = '')
            price = input()
            if(len(price.strip())>0):
                try:
                    price = float(price.strip())
                    break
                except:
                    printMessage('❗Introduce un precio correcto')

            else: printMessage('❗Introduce un precio correcto')

        return Event(date, maxDate, location, province, organizer, totalKM, price)

    def showInfoPartners(self, listOfUser: dict):
        printMessage('\nLista de Socios', 'cyan')
        printMessage('===============')
        for user in sorted(listOfUser.items(), key=lambda x: x[1].partner.fullName):
            printMessage(f'{listOfUser.get(user[0])}\n')
            pause()

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
                pause()
        else: printMessage(f'❗El año {year} no existe en los registros')

    def requestDni(self):
        while True:
            printMessage(f'Introduce un dni: ')
            print(">>> ", end = '')
            dni = input()
            
            if(self.controller.existDni(dni)): return dni
            else: printMessage('❗Introduce un dni valido') 

    def showDataPay(self, data: list):
        if( data != None ):
            printMessage(f'Pago de Cuota de {data[0]}', 'cyan')
            printMessage('============================', 'cyan')
            printMessage(f'{data[1]}\n')
        else: printMessage('❗La cuota de este año ya esta pagada\n')

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

        #Request DNI
        while(True):
            printMessage('Introduce un dni:', 'yellow')
            print(">>> ", end = '')
            dni = input()
            if(checkRegex(dni, 'dni')): 
                if(not(self.controller.existDni(dni))): break
                else: printMessage('❗Introduce un dni que no exista ya')
            else: printMessage('❗Introduce un dni valido')

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
        
        self.controller.saveNewPartner(User(fullname, address, phonenumber, email, dni, password, isAdmin, True))
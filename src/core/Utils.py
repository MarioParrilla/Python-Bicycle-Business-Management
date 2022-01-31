import os, re
from src.view.View import printMessage

helpData = { 
    "-u, --user": 'Sirve para indicar el usuario para iniciar sesion. Debe ir antes de la contraseña.' ,
    "-p, --password": 'Sirve para indicar la contraseña para iniciar sesion. Debe ir despues del usuario.' ,
    "-A, --admin": 'Sirve para indicar que vas a iniciar sesion como administrator. Debe ir despues de la contraseña.' ,
    "-h, --help": 'Nos mostrará la explicación de los comandos del programa. Debe ir tras el nombre del programa.'
    }

def showWarnHelp(): printMessage("❔Puedes usar -h o --help para ver los flags disponibles con su infomación.")

def error(msg: str):
    printMessage(f"❗Error: {msg}", 'red')
    showWarnHelp()

def help(): 
    printMessage("-------- ❔Ayuda -------- \n", 'cyan')
    for commandTitle in helpData.keys():
        printMessage(f"   { commandTitle }", 'yellow')
        printMessage(f"\t { helpData[commandTitle] } \n")
    printMessage("-------------------------", 'cyan')

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def checkArguments(args: str):

    if len(args) == 1: 
        error("Para iniciar sesion se necesita indicar un usuario y una constraseña.")
        
    elif(len(args) == 2 and (args[1] == "-u" or args[1] == "--user" or args[1] == "-p" or args[1] == "--password" 
            or args[1] == "-h" or args[1] == "--help")):

        if(args[1]   == "-h" or args[1] == "--help"): help()

        elif(args[1] == "-u" or args[1] == "--user"): 
            error("¡Debe introducir un usuario y una constraseña!.")

        elif(args[1] == "-p" or args[1] == "--password"): 
            error("¡Debe introducir primero un usuario!.")
            

    elif(len(args) == 3):
        if(args[1] == "-u" or args[1] == "--user"):
            error("¡Debe introducir una contraseña para acceder a la cuenta!.")
        elif(args[1] == "-p" or args[1] == "--password"):
            error("¡Debe introducir primero un usuario!.")

    elif(len(args) == 4):

        if(args[1] == "-p" or args[1] == "--password"): 
            error("¡Debe introducir primero un usuario!.")
        
        elif( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") ):
            error("¡Debe introducir una constraseña!.")
        
        else: error()

    elif(len(args) == 5):

        if(args[1] == "-p" or args[1] == "--password"): 
            error("¡Debe introducir primero un usuario!.")
        
        elif( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") ):
            return True
        
        else: error()

    elif(len(args) == 6):

        if( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") and (args[5] == "-A" or args[5] == "--admin")):
            return True
        
        else: error("Has introducido un parametro no valido o en una posicion no valida.")
            

    else: error("Has introducido un parametro no valido o en una posicion no valida.")

def checkRegex(patron: str, type: str):
    if( type == 'phonenumber' ): return bool(re.compile('(\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}').match(patron))
    elif( type == 'dni' ): return bool(re.compile('^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$').match(patron))
    elif( type == 'email' ): return bool(re.compile('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}').match(patron))
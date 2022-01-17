from src.view.View import View

helpData = { 
    "-u, --user": 'Sirve para indicar el usuario para iniciar sesion. Debe ir antes de la contraseña.' ,
    "-p, --password": 'Sirve para indicar la contraseña para iniciar sesion. Debe ir despues del usuario.' ,
    "-A, --admin": 'Sirve para indicar que vas a iniciar sesion como administrator. Debe ir despues de la contraseña.' ,
    "-h, --help": 'Nos mostrará la explicación de los comandos del programa. Debe ir tras el nombre del programa.'
    }

def showWarnHelp(): View.printMessage("❔Puedes usar -h o --help para ver los flags disponibles con su infomación.")

def error(msg: str):
    View.printMessage(f"❗Error: {msg}", 'red')
    showWarnHelp()

def help(): 
    View.printMessage("-------- ❔Ayuda -------- \n", 'cyan')
    for commandTitle in helpData.keys():
        View.printMessage(f"   { commandTitle }", 'yellow')
        View.printMessage(f"\t { helpData[commandTitle] } \n")
    View.printMessage("-------------------------", 'cyan')

def checkArguments(args: str):

    if len(args) == 1: 
        error("Para iniciar sesion se necesita indicar un usuario y una constraseña.")
        showWarnHelp()
        
    elif(len(args) == 2 and (args[1] == "-u" or args[1] == "--user" or args[1] == "-p" or args[1] == "--password" 
            or args[1] == "-h" or args[1] == "--help")):

        if(args[1]   == "-h" or args[1] == "--help"): help()

        elif(args[1] == "-u" or args[1] == "--user"): 
            error("¡Debe introducir un usuario y una constraseña!.")
            showWarnHelp()

        elif(args[1] == "-p" or args[1] == "--password"): 
            error("¡Debe introducir primero un usuario!.")
            showWarnHelp()

    elif(len(args) == 3):
        if(args[1] == "-u" or args[1] == "--user"):
            error("¡Debe introducir una contraseña para acceder a la cuenta!.")
            showWarnHelp()
        elif(args[1] == "-p" or args[1] == "--password"):
            error("¡Debe introducir primero un usuario!.")
            showWarnHelp()

    elif(len(args) == 4):

        if(args[1] == "-p" or args[1] == "--password"): 
            error("¡Debe introducir primero un usuario!.")
            showWarnHelp()
        
        elif( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") ):
            print("[DEV] LOGIN SIN CONTRASEÑA")
        
        else: error()

    elif(len(args) == 5):

        if(args[1] == "-p" or args[1] == "--password"): 
            error("¡Debe introducir primero un usuario!.")
            showWarnHelp()
        
        elif( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") ):
            print("[DEV] LOGIN CON CONTRASEÑA")
        
        else: error()

    elif(len(args) == 6):

        if( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") and (args[5] == "-A" or args[5] == "--admin")):
            print("[DEV] LOGIN ADMIN")
        
        else: error("Has introducido un parametro no valido o en una posicion no valida.")
            

    else: error("Has introducido un parametro no valido o en una posicion no valida.")
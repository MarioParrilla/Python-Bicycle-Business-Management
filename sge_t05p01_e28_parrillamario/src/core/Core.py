def showWarnHelp(): print("❔ Puedes usar -h o --help para ver los flags disponibles con su infomación.")

def error():
    print("❗ Error: Has introducido un parametro no valido o en una posicion no valida.")
    showWarnHelp()

def help(): print("❔ Ayuda")

def checkArguments(args):

    if len(args) == 1: 
        print("❗ Para iniciar sesion se necesita indicar un usuario y una constraseña.")
        showWarnHelp()
        
    elif(len(args) == 2 and (args[1] == "-u" or args[1] == "--user" or args[1] == "-p" or args[1] == "--password" 
            or args[1] == "-h" or args[1] == "--help")):

        if(args[1]   == "-h" or args[1] == "--help"): help()

        elif(args[1] == "-u" or args[1] == "--user"): 
            print("❗ ¡Debe introducir un usuario y una constraseña!.")
            showWarnHelp()

        elif(args[1] == "-p" or args[1] == "--password"): 
            print("❗ ¡Debe introducir primero un usuario!.")
            showWarnHelp()

    elif(len(args) == 3 and (args[1] == "-u" or args[1] == "--user")):
            print("❗ ¡Debe introducir una contraseña para acceder a la cuenta!.")
            showWarnHelp()

    elif(len(args) == 4):

        if(args[1] == "-p" or args[1] == "--password"): 
            print("❗ ¡Debe introducir primero un usuario!.")
            showWarnHelp()
        
        elif( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") ):
            print("[DEV] LOGIN SIN CONTRASEÑA")
        
        else: error()

    elif(len(args) == 5):

        if(args[1] == "-p" or args[1] == "--password"): 
            print("❗ ¡Debe introducir primero un usuario!.")
            showWarnHelp()
        
        elif( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") ):
            print("[DEV] LOGIN CON CONTRASEÑA")
        
        else: error()

    elif(len(args) == 6):

        if( (args[1] == "-u" or args[1] == "--user") and (args[3] == "-p" or args[3] == "--password") and (args[5] == "-A" or args[5] == "--admin")):
            print("[DEV] LOGIN ADMIN")
        
        else: error()
            

    else: error()

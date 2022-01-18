from colorama import Fore

class View:

    def __init__(self):
        pass

    def screen(clubName, userName, lastAccess, admin = False):
        if(admin):
            print(Fore.BLUE + '*************************************' + Fore.RESET)
            print(Fore.RED + '        Zona de Administración' + Fore.RESET)
            print(Fore.BLUE + '*************************************' + Fore.RESET)
            print(Fore.YELLOW + 'APP: ' + Fore.RESET + clubName + Fore.RESET)
            print(Fore.YELLOW + 'USUARIO: ' + Fore.RESET + userName + Fore.RESET)
            print(Fore.YELLOW + 'Ultimo Acc.: ' + Fore.RESET + lastAccess + Fore.RESET)
            print(Fore.BLUE + '*************************************\n' + Fore.RESET)
        else:
            print(Fore.BLUE + '*************************************' + Fore.RESET)
            print(Fore.YELLOW + 'APP: ' + Fore.RESET + clubName + Fore.RESET)
            print(Fore.YELLOW + 'USUARIO: ' + Fore.RESET + userName + Fore.RESET)
            print(Fore.YELLOW + 'Ultimo Acc.: ' + Fore.RESET + lastAccess + Fore.RESET)
            print(Fore.BLUE + '*************************************\n' + Fore.RESET)


    def printMessage(msg: str, color: str = 'white'):
        if(color.lower()   == 'white'):  print(Fore.WHITE + msg + Fore.RESET)
        elif(color.lower() == 'red'):    print(Fore.RED + msg + Fore.RESET)
        elif(color.lower() == 'blue'):   print(Fore.BLUE + msg + Fore.RESET)
        elif(color.lower() == 'cyan'):   print(Fore.CYAN + msg + Fore.RESET)
        elif(color.lower() == 'green'):  print(Fore.GREEN + msg + Fore.RESET)
        elif(color.lower() == 'yellow'): print(Fore.YELLOW + msg + Fore.RESET)
from colorama import Fore

class View:

    def __init__(self):
        pass

    def printMessage(msg: str, color: str = 'white'):
        if(color.lower()   == 'white'): print(Fore.WHITE + msg +Fore.RESET)
        elif(color.lower() == 'red'): print(Fore.RED + msg +Fore.RESET)
        elif(color.lower() == 'cyan'): print(Fore.CYAN + msg +Fore.RESET)
        elif(color.lower() == 'green'): print(Fore.GREEN + msg +Fore.RESET)
        elif(color.lower() == 'yellow'): print(Fore.YELLOW + msg +Fore.RESET)
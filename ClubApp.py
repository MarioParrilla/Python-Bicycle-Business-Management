import sys, os
from src.view.View import View
from src.core.Utils import checkArguments  

if __name__ == "__main__":
    os.system("cls")
    if(checkArguments(sys.argv)): View.printMessage("Acceso Concedido ✅", 'green')
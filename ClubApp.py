import sys
from src.core.Utils import checkArguments, clear
from src.controller.UserController import UserController
from src.controller.AdminController import AdminController
from src.model.Club import Club

if __name__ == "__main__":
    clear()
    if(checkArguments(sys.argv)):
        club = Club('Los satanases del Infierno', '325325', 'Madrid', [], [], 0)
        if(len(sys.argv)   == 5): 
            userController = UserController(club, sys.argv[2], sys.argv[4])
            userController.init()
        elif(len(sys.argv) == 6): 
            adminController = AdminController(club, sys.argv[2], sys.argv[4])
            adminController.init()

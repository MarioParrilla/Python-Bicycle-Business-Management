import sys, os
from src.core.Utils import checkArguments  
from src.controller.UserController import UserController
from src.controller.AdminController import AdminController

if __name__ == "__main__":
    os.system("cls")
    if(checkArguments(sys.argv)):
        if(len(sys.argv)   == 5): 
            userController = UserController(None, sys.argv[2], sys.argv[4])
            userController.init()
        elif(len(sys.argv) == 5): 
            adminController = AdminController(None, sys.argv[2], sys.argv[4])
            adminController.init()

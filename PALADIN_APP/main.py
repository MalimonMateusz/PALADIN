from PyQt5.QtWidgets import QApplication
from PALADIN_APP.view.LoginWindow import LoginWindow
from controller.AppController import AppController




def main():

    appController = AppController()
    appController.run()



if __name__ == "__main__":
    main()
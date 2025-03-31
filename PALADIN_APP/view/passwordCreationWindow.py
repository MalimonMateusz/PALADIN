from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from PALADIN_APP.view.LoginWindow import show_error_message


class passwordCreationWindow(QDialog):

    @staticmethod
    def show_error_message(title, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setText(message)
        error_msg.setWindowTitle(title)
        error_msg.exec_()

    def __init__(self,app_controller):
        super().__init__()
        self.app_controller = app_controller
        loadUi("C:/Users\Lichw\Desktop\Studia\Python\PALADIN\PALADIN_APP/view/ui\passwordCreationWindow.ui",self)
        self.returnButton.clicked.connect(self.return_to_mainWindow)
        self.passwordTextbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatPasswordTextbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.addNewPasswordButton.clicked.connect(self.add_password)


    def add_password(self):
        name = self.nameTextbox.text()
        login = self.loginTextbox.text()
        password = self.passwordTextbox.text()
        repeatPassword = self.repeatPasswordTextbox.text()

        if name.strip() == "" or login.strip() == "" or password.strip() == "" or repeatPassword.strip() == "":
            show_error_message("Error", "Fill that textboxes broski")
            return
        elif password != repeatPassword:
            show_error_message("Error", "Passwords does not match")
            return
        else:
            print("A")
            self.app_controller.add_password(name,login,password)
            self.accept()




    def return_to_mainWindow(self):
        self.accept()








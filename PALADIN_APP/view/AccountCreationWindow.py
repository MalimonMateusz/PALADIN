import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from PALADIN_APP.view.LoginWindow import show_error_message


class AccountCreationWindow(QDialog):

    @classmethod
    def show_error_message(self, title, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setText(message)
        error_msg.setWindowTitle(title)
        error_msg.exec_()


    def __init__(self, app_controller):
        super().__init__()
        self.app_controller = app_controller
        loadUi("C:/Users\Lichw\Desktop\Studia\Python\PALADIN\PALADIN_APP/view/ui/accountCreationWindow.ui", self)
        self.createAccountButton.clicked.connect(self.create_account)
        self.returnButton.clicked.connect(self.return_to_login)
        self.passwordTextbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatPasswordTextbox.setEchoMode(QtWidgets.QLineEdit.Password)



    def create_account(self):
        login = self.loginTextbox.text()
        password = self.passwordTextbox.text()
        password2 = self.repeatPasswordTextbox.text()\

        if login.strip() == "" or password.strip() == "":
            show_error_message("ERROR", "FILL THAT GAPS BROSKI")
            return

        if password != password2:
            show_error_message("ERROR", "PASSWORDS DOES NOT MATCH")
            return
        else:
            print(f"Account Created {login} {password}")
            self.app_controller.create_account(login, password)


    def return_to_login(self):
        self.app_controller.open_login_window()



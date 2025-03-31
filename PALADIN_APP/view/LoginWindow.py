import bcrypt
import mysql
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector



def show_error_message(title, message):
    error_msg = QMessageBox()
    error_msg.setIcon(QMessageBox.Critical)
    error_msg.setText(message)
    error_msg.setWindowTitle(title)
    error_msg.exec_()


class LoginWindow(QDialog):

    def __init__(self, app_controller):
        super().__init__()
        self.app_controller = app_controller
        loadUi("C:/Users\Lichw\Desktop\Studia\Python\PALADIN\PALADIN_APP/view/ui\login.ui", self)
        self.setWindowIcon(QIcon("C:/Users\Lichw\Desktop\Studia\Python\PALADIN\photos\mainWindowIcon.png"))
        self.loginButton.clicked.connect(self.login_function)
        self.passwordTextbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.noAccountButton.clicked.connect(self.create_account)
        self.adjustSize()
        self.setFixedSize(600,650)








    def login_function(self):
        login=self.loginTextbox.text()
        password=self.passwordTextbox.text()
        if login.strip() == "" and password.strip() == "":
            show_error_message("ERROR", "Fill dat textboxs broski")
            return
        else:
            self.app_controller.try_loging_in(login, password)

    def create_account(self):
        self.app_controller.open_create_account_window()












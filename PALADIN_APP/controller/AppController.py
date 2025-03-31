import sys

from PyQt5.QtGui import QIcon

from PALADIN_APP.model.DataBase import DataBase
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox

from PALADIN_APP.view.AccountCreationWindow import AccountCreationWindow
from PALADIN_APP.view.LoginWindow import LoginWindow
from PALADIN_APP.view.MainWindow import MainWindow
from PALADIN_APP.view.passwordCreationWindow import passwordCreationWindow
from PALADIN_APP.view.passwordWindow import PasswordWindow


class AppController:

    @classmethod
    def show_error_message(self, title, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setText(message)
        error_msg.setWindowTitle(title)
        error_msg.exec_()


    def __init__(self):
        self.logged_user = None

        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon("C:/Users\Lichw\Desktop\Studia\Python\PALADIN\photos\mainWindowIcon.png"))
        self.widget = QtWidgets.QStackedWidget()

        self.db = DataBase()
        self.current_Window = LoginWindow(self)
        self.widget.addWidget(self.current_Window)


    def run(self):
        self.widget.show()
        sys.exit(self.app.exec_())

    def set_current_window(self, window):
        self.current_Window = window

    def try_loging_in(self,login, password):
        login_status, user_id = self.db.try_loging_in(login, password)
        if login_status:
            self.logged_user = user_id
            self.current_Window = MainWindow(self, login)
            self.widget.addWidget(self.current_Window)
            self.widget.setCurrentIndex(self.widget.currentIndex()+1)
            self.widget.setFixedSize(800, 600)
        else:
            self.show_error_message("ERROR", "INCORRECT LOGIN OR PASSWORD")

    def open_create_account_window(self):
        self.current_Window = AccountCreationWindow(self)
        self.widget.addWidget(self.current_Window)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def create_account(self, login, password):
        self.db.create_account(login, password)

    def open_login_window(self):

        self.current_Window = LoginWindow(self)
        self.widget.addWidget(self.current_Window)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def create_password(self):
        password_creation_window = passwordCreationWindow(self)
        password_creation_window.exec_()
        self.current_Window.update_list_widget()


    def log_out(self):
        self.logged_user = None
        self.current_Window = LoginWindow(self)
        self.widget.addWidget(self.current_Window)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
        self.widget.setFixedSize(600,650)

    def add_password(self, name,login, password):
        self.db.create_password(name, login, password, self.logged_user)

    def get_logins(self):
        return self.db.get_logins(self.logged_user)

    def show_password_details(self, name):
        login, password = self.db.get_password(self.logged_user,name)
        passwordWindow = PasswordWindow(name,login, password)
        passwordWindow.exec_()










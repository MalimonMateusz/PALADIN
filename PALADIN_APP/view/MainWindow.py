from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.uic import loadUi

from PALADIN_APP.view.passwordCreationWindow import passwordCreationWindow


class MainWindow(QMainWindow):


    def __init__(self, app_controller,login):
        super().__init__()
        self.app_controller = app_controller
        loadUi("C:/Users\Lichw\Desktop\Studia\Python\PALADIN\PALADIN_APP/view/ui\MainWindow.ui",self)
        self.userNameLabel.setText(login)
        print(self.app_controller.get_logins())
        self.addNewPasswordButton.clicked.connect(self.open_password_creation_window)
        self.logOutButton.clicked.connect(self.log_out)
        self.listWidget.itemClicked.connect(self.show_password_details)

        self.update_list_widget()

    def update_list_widget(self):
        self.listWidget.clear()
        for service in self.app_controller.get_logins():
            self.listWidget.addItem(service[0])

    def open_password_creation_window(self):
        self.app_controller.create_password()

    def log_out(self):
        self.app_controller.log_out()

    def show_password_details(self, item):
        item_name = item.text()
        self.app_controller.show_password_details(item_name)











from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class PasswordWindow(QDialog):
    def __init__(self,name, login, password):
        super().__init__()
        loadUi("C:/Users\Lichw\Desktop\Studia\Python\PALADIN\PALADIN_APP/view/ui\passwordWindow.ui",self)
        self.nameLabel.setText(f"{name}")
        self.loginLabel.setText(f"{login}")
        self.passwordLabel.setText(f"{password}")
        self.returnButton.clicked.connect(self.close)
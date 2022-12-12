from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QDialog

from controllers.Login import UiDialogLogin

from controllers.LoginController import LoginController
from controllers.SignupController import SignupController
from controllers.MainController import MainController

import sys


class Application:
    def __init__(self):
        self._TITTLE = "Application v0.20221212"
        self.user = ""

        useGUI = not '-no-gui' in sys.argv
        self.__qapplication = QApplication(sys.argv) if useGUI else QCoreApplication(sys.argv)
        self.__qwidget = None
        self.__ui = None

    def play(self):
        self.ui_config(QDialog(), UiDialogLogin(self))
        return self.__qapplication.exec_()

    def play_without_qwidget(self):
        self.ui_config_without_qwidget("login")
        return self.__qapplication.exec_()

    def ui_config(self, __qwidget, __ui):
        if __qwidget and __ui:
            self.__qwidget = __qwidget
            self.__ui = __ui
            self.__ui.setupUi(self.__qwidget)
            self.__qwidget.show()

    def ui_config_without_qwidget(self, __ui):
        ui = self.__ui
        if __ui == "login":
            self.__ui = LoginController(self)
        elif __ui == "signup":
            self.__ui = SignupController(self)
        elif __ui == "main":
            self.__ui = MainController(self)

        if ui:
            ui.close()
        self.__ui.show()



if __name__ == '__main__':
    application = Application()
    application.play_without_qwidget()

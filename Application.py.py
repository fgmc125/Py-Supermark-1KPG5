from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication

from controllers.AddCategoryController import AddCategoryController
from controllers.AddProductController import AddProductController
from controllers.LoginController import LoginController
from controllers.SignupController import SignupController
from controllers.MainController import MainController

import sys


class Application:
    def __init__(self):
        self.TITTLE = "v0.20221215"
        self.user = ""
        self.is_staff = None
        self.is_superuser = None

        useGUI = not '-no-gui' in sys.argv
        self.__qapplication = QApplication(sys.argv) if useGUI else QCoreApplication(sys.argv)
        self.__qwidget = None
        self.__ui = None
        self.__ui_modal = None

    def play(self):
        self.ui_config("login")
        return self.__qapplication.exec_()

    def ui_config_modal(self, __ui_modal):
        ui = self.__ui_modal
        if __ui_modal:
            if __ui_modal == "new_product":
                self.__ui_modal = AddProductController(self)
            elif __ui_modal == "new_category":
                self.__ui_modal = AddCategoryController(self)
            elif __ui_modal == "new_user":
                self.__ui_modal = AddCategoryController(self)

            if ui:
                ui.close()
            self.__ui_modal.setModal(True)
            self.__ui_modal.show()
        else:
            if ui:
                ui.close()



    def ui_config(self, __ui):
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

    def getTitle(self):
        return self.TITTLE


if __name__ == '__main__':
    application = Application()
    application.play()

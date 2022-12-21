from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication

from controllers.AddCategoryController import AddCategoryController
from controllers.AddProductController import AddProductController
from controllers.AddUserController import AddUserController
from controllers.AlertController import AlertController
from controllers.EditCategoryController import EditCategoryController
from controllers.EditProductController import EditProductController
from controllers.EditUserController import EditUserController
from controllers.LoginController import LoginController
from controllers.SignupController import SignupController
from controllers.MainController import MainController

import sys

from controllers.UserController import UserController
from mysqlhelper.Conector import Conexion


class Application:
    def __init__(self):
        self.__connector = None
        self.TITTLE = "v0.20221220"

        self.user_id = None
        self.user = ""
        self.is_staff = None
        self.is_superuser = None

        self.categories_data = None
        self.products_data = dict()
        self.shopping_cart = None

        self.load_data()

        useGUI = not '-no-gui' in sys.argv
        self.__qapplication = QApplication(sys.argv) if useGUI else QCoreApplication(sys.argv)
        self.__qwidget = None
        self.__ui = None
        self.__ui_modal = None

    def play(self):
        self.ui_config("login")
        return self.__qapplication.exec_()

    def ui_config_modal(self, __ui_modal, __id=None):
        ui = self.__ui_modal
        if __ui_modal:
            if __ui_modal == "new_product":
                self.__ui_modal = AddProductController(self)
            elif __ui_modal == "edit_product":
                self.__ui_modal = EditProductController(self, product=__id)
            elif __ui_modal == "remove_product":
                self.__ui_modal = AlertController(self, id=__id, from_db='bhhj3cug6bdknptqdl7k.product_db', message="¿Esta seguro que desea eliminar el producto de la base de datos?")
            elif __ui_modal == "new_category":
                self.__ui_modal = AddCategoryController(self)
            elif __ui_modal == "edit_category":
                self.__ui_modal = EditCategoryController(self, category=__id)
            elif __ui_modal == "remove_category":
                self.__ui_modal = AlertController(self, id=__id, from_db='bhhj3cug6bdknptqdl7k.category_db', message="¿Esta seguro que desea eliminar la categoría de la base de datos?")
            elif __ui_modal == "view_user":
                self.__ui_modal = UserController(self, user=__id)
            elif __ui_modal == "new_user":
                self.__ui_modal = AddUserController(self)
            elif __ui_modal == "edit_user":
                self.__ui_modal = EditUserController(self, user=__id)
            elif __ui_modal == "remove_user":
                self.__ui_modal = AlertController(self, id=__id, from_db='bhhj3cug6bdknptqdl7k.user_db', message="¿Esta seguro que desea eliminar el usuario de la base de datos?")
            elif __ui_modal == "remove_cart_item":
                self.__ui_modal = AlertController(self, id=__id, from_db='bhhj3cug6bdknptqdl7k.shopping_cart_db', message="¿Esta seguro que desea eliminar el producto de tu carrito?")

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

    def getMainView(self):
        print(type(self.__ui) == MainController)
        if type(self.__ui) == MainController:
            return self.__ui

    def load_data(self):
        self.__connector = Conexion()
        print("DEBUG: Iniciando carga de datos:")
        print("DEBUG: 1 de 2: Categorías")
        if self.__connector.is_connected():
            sql = "SELECT * FROM bhhj3cug6bdknptqdl7k.category_db"
            self.categories_data = self.__connector.run_query(sql)

        print("DEBUG: 100%")
        print("DEBUG: 2 de 2: productos")
        cnt = 1
        for category in self.categories_data:
            if self.__connector.is_connected():
                sql = """SELECT * FROM bhhj3cug6bdknptqdl7k.product_db WHERE family_id = '%s'"""
                data = [category[0]]
                self.products_data[category[1]] = self.__connector.run_query(query=sql, data=data)

                print("DEBUG: %", int(cnt*100/len(self.categories_data)))
                cnt +=1
        print("DEBUG: Fin de carga de datos")
        self.__connector.close()


if __name__ == '__main__':
    application = Application()
    application.play()

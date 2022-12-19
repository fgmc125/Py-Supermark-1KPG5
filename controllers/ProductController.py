from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class ProductController(QtWidgets.QWidget):
    def __init__(self, main_controller, product, category):
        super(ProductController, self).__init__()
        loadUi('views/ProductView.ui', self)
        self.__main_controller = main_controller
        self.__product_data = product
        self.__category = category
        self.__setupUiComponents()

    def __setupUiComponents(self):
        labels = self.findChildren(QtWidgets.QLabel)
        labels[0].setText(self.__product_data[1])
        labels[1].setText(self.__category)

        self.btn_add_to_cart.clicked.connect(self.__show_items)
        self.btn_buy.clicked.connect(self.__show_items)
        self.btn_send_message.clicked.connect(self.__show_items)
        self.btn_remove.clicked.connect(self.__remove)



    def __show_items(self):
        pass #self.__main_controller._reformat_content(self.__category[1], self.__product_data)

    def __remove(self):
        print("id a borrar: ", self.__product_data[0])
        self.__main_controller.ui_config_modal(ui_modal='remove_product', id=self.__product_data[0])
        self.__main_controller._load_content_area()

    def __edit(self):
        pass

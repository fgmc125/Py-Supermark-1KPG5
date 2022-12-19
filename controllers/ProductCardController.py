from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class ProductCardController(QtWidgets.QWidget):
    def __init__(self, main_controller, product):
        super(ProductCardController, self).__init__()
        loadUi('views/CardView.ui', self)
        self.__main_controller = main_controller
        self.__product_data = product
        self.__setupUiComponents()

    def __setupUiComponents(self):

        print(self.__product_data)
        labels = self.findChildren(QtWidgets.QLabel)
        labels[0].setText("$ " + str(self.__product_data[0][3]).replace(',', '.'))
        labels[1].setText(self.__product_data[0][1])

        self.btn_show_items.setText("ver más")
        self.btn_show_items.clicked.connect(self.__show_items)


    def __show_items(self):
        pass #self.__main_controller._reformat_content(self.__category[1], self.__product_data)

    def __remove(self):
        pass

    def __edit(self):
        pass

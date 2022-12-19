from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class CategoryCardController(QtWidgets.QWidget):
    def __init__(self, main_controller, category, product_data):
        super(CategoryCardController, self).__init__()
        loadUi('views/CardView.ui', self)
        self.__main_controller = main_controller
        self.__product_data = product_data
        self.__category = category
        self.__setupUiComponents()

    def __setupUiComponents(self):
        labels = self.findChildren(QtWidgets.QLabel)
        labels[0].setText(self.__category[1])
        labels[1].setText(str(len(self.__product_data)) + " artículos")

        self.btn_show_items.clicked.connect(self.__show_items)

    def __show_items(self):
        self.__main_controller._reformat_content(self.__category[1], self.__product_data)

    def __remove(self):
        pass

    def __edit(self):
        pass

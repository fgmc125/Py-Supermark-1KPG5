from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class CardController(QtWidgets.QWidget):
    def __init__(self, category):
        super(CardController, self).__init__()
        loadUi('views/CardView.ui', self)
        self.product_data = None
        self.__setupUiComponents(category)

    def __setupUiComponents(self, category):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = """SELECT * FROM bhhj3cug6bdknptqdl7k.product_db WHERE family_id = %s"""
            data = [category[0]]
            self.product_data = self._connector.run_query(query=sql, data=data)

        labels = self.findChildren(QtWidgets.QLabel)
        labels[0].setText(category[1])
        labels[1].setText(str(len(self.product_data)) + " artículos")

        self._connector.close()

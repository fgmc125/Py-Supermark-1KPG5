from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class CartCardController(QtWidgets.QWidget):
    def __init__(self, main_controller, user, item):
        super(CartCardController, self).__init__()
        loadUi('views/CardView3.ui', self)
        self.__main_controller = main_controller
        self.__shopping_cart_item = item
        self.__product_data = None
        self.__user = user

        self.__setupUiComponents()

    def __setupUiComponents(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = """SELECT * FROM bhhj3cug6bdknptqdl7k.product_db WHERE id = %s"""
            data = [str(self.__shopping_cart_item[3])]
            self.__product_data = self._connector.run_query(sql, data)
            self._connector.close()
        self.sbx_amount.setMaximum(self.__product_data[0][4])
        self.sbx_amount.setValue(self.__shopping_cart_item[1])
        self.sbx_amount.setPrefix("$ ")
        self.sbx_amount.setSuffix(" unidades")
        self.sbx_amount.setAlignment(Qt.AlignCenter)
        self.sbx_amount.valueChanged.connect(self.__update)

        labels = self.findChildren(QtWidgets.QLabel)
        labels[0].setText(self.__product_data[0][1])
        labels[1].setText("Total : " + str(self.__product_data[0][3]*self.__shopping_cart_item[1]))

        if not self.__main_controller._application.is_staff:
            self.btn_action.clicked.connect(self.__action_add_subtract)
            self.btn_remove.clicked.connect(self.__remove)
            if self.__shopping_cart_item[2] == 0:
                self.btn_save.setText("Guardar")
                self.btn_save.clicked.connect(self.__save_item_from_cart)
            else:
                self.btn_save.setText("Al Carrito")
                self.btn_save.clicked.connect(self.__unsave_item_from_cart)

    def __update(self, value):
        self.lbl_total.setText("Total : $ " + str(self.__product_data[0][3]*value))
        icon = QtGui.QIcon()
        if value == self.__shopping_cart_item[1]:
            self.btn_action.setStyleSheet("QPushButton {\n"
                                          "    color : #FFFFFF;\n"
                                          "    border-style : solid;\n"
                                          "    border-radius: 5px;\n"
                                          "    min-height : 40px;\n"
                                          "    font : 77 18px \"Arial\";\n"
                                          "    background-color : orange;\n"
                                          "    padding-left : 20px;\n"
                                          "    padding-right : 20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    border: 1px solid #FFF;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color : transparent;\n"
                                          "    color : orange;\n"
                                          "    border: 1px solid orange;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "")
            icon.addPixmap(QtGui.QPixmap(":/icon/assets/icon/cart-shopping3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_action.setIcon(icon)
        elif value < self.__shopping_cart_item[1]:
            self.btn_action.setStyleSheet("QPushButton {\n"
                                          "    color : #FFFFFF;\n"
                                          "    border-style : solid;\n"
                                          "    border-radius: 5px;\n"
                                          "    min-height : 40px;\n"
                                          "    font : 77 18px \"Arial\";\n"
                                          "    background-color : red;\n"
                                          "    padding-left : 20px;\n"
                                          "    padding-right : 20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    border: 1px solid #FFF;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color : transparent;\n"
                                          "    color : red;\n"
                                          "    border: 1px solid red;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "")
            icon.addPixmap(QtGui.QPixmap(":/icon/assets/icon/cart-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_action.setIcon(icon)
        elif value > self.__shopping_cart_item[1]:
            self.btn_action.setStyleSheet("QPushButton {\n"
                                          "    color : #FFFFFF;\n"
                                          "    border-style : solid;\n"
                                          "    border-radius: 5px;\n"
                                          "    min-height : 40px;\n"
                                          "    font : 77 18px \"Arial\";\n"
                                          "    background-color : #42B72A;\n"
                                          "    padding-left : 20px;\n"
                                          "    padding-right : 20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    border: 1px solid #FFF;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color : transparent;\n"
                                          "    color : #42B72A;\n"
                                          "    border: 1px solid #42B72A;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "")
            icon.addPixmap(QtGui.QPixmap(":/icon/assets/icon/cart-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_action.setIcon(icon)

    def __action_add_subtract(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            if self.sbx_amount.value() != self.__shopping_cart_item[1]:
                sql = "UPDATE bhhj3cug6bdknptqdl7k.shopping_cart_db  SET " \
                      "amount = " + str(self.sbx_amount.value()) \
                      + " WHERE id = '" + str(self.__shopping_cart_item[0]) + "'"

                self._connector.run_query(query=sql)
                self._connector.close()

                print("Se actualizo el item.")
        else:
            alert = " * ¡ERROR! No se pudo realizar la coneccion."
            print(alert)

    def __save_item_from_cart(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "UPDATE bhhj3cug6bdknptqdl7k.shopping_cart_db  SET saved = " + 'True' \
                  + " WHERE id = '" + str(self.__shopping_cart_item[0]) + "'"

            self._connector.run_query(query=sql)
            self._connector.close()

    def __unsave_item_from_cart(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "UPDATE bhhj3cug6bdknptqdl7k.shopping_cart_db  SET saved = " + 'False' \
                  + " WHERE id = '" + str(self.__shopping_cart_item[0]) + "'"

            self._connector.run_query(query=sql)
            self._connector.close()

    def __remove(self):
        self.__main_controller.ui_config_modal(ui_modal='remove_cart_item', id=self.__shopping_cart_item[0])

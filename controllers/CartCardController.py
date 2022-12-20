from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class CartCardController(QtWidgets.QWidget):
    def __init__(self, main_controller, user, product_data):
        super(CartCardController, self).__init__()
        loadUi('views/CardView.ui', self)
        self.__main_controller = main_controller
        self.__product_data = product_data
        self.__user = user

        self.__setupUiComponents()

    def __setupUiComponents(self):
        if not self.__main_controller._application.is_staff:
            self.btn_show_items.deleteLater()

            self.sbx_current = QtWidgets.QSpinBox(self.frame_10)
            self.sbx_current.setStyleSheet("QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox {\n"
                                           "    background-color : transparent;\n"
                                           "    border : 1px solid #DADDE1;\n"
                                           "    border-radius : 5px;\n"
                                           "    color : #616161;\n"
                                           "    min-height : 40px;\n"
                                           "    font : 77 18px \"Arial\";\n"
                                           "}")
            self.sbx_current.setObjectName("sbx_current")
            self.horizontalLayout_11.addWidget(self.sbx_current)
            self.sbx_current.setMaximum(self.__product_data[4])

            self.btn_a = QtWidgets.QPushButton(self.frame_10)
            self.btn_a.setMinimumSize(QtCore.QSize(40, 40))
            self.btn_a.setMaximumSize(QtCore.QSize(40, 40))
            self.btn_a.setStyleSheet("QPushButton {\n"
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
                                     "")
            self.btn_a.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icon/assets/icon/square-pen1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_a.setIcon(icon)
            self.btn_a.setObjectName("btn_a")
            self.horizontalLayout_11.addWidget(self.btn_a)

            self.btn_b = QtWidgets.QPushButton(self.frame_10)
            self.btn_b.setMinimumSize(QtCore.QSize(40, 40))
            self.btn_b.setMaximumSize(QtCore.QSize(40, 40))
            self.btn_b.setStyleSheet("QPushButton {\n"
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
            self.btn_b.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/icon/assets/icon/square-xmark1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_b.setIcon(icon1)
            self.btn_b.setObjectName("btn_b")
            self.horizontalLayout_11.addWidget(self.btn_b)

        labels = self.findChildren(QtWidgets.QLabel)
        labels[0].setText(self.__category[1])
        labels[1].setText(str(len(self.__product_data)) + " artículos")

        self.btn_show_items.clicked.connect(self.__show_items)
        if self.__main_controller._application.is_staff:
            self.btn_a.clicked.connect(self.__edit)
            self.btn_b.clicked.connect(self.__remove)

    def __show_items(self):
        self.__main_controller._reformat_content(self.__category[1], self.__product_data)

    def __remove(self):
        self.__main_controller.ui_config_modal(ui_modal='remove_category', id=self.__category[0])
        self.__main_controller._load_content_area()

    def __edit(self):
        self.__main_controller.ui_config_modal("edit_category", id=self.__category[0])

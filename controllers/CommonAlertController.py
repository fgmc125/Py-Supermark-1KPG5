from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class CommonAlertController(QDialog):
    def __init__(self, __application, message):
        super(CommonAlertController, self).__init__()
        self.__application = __application
        loadUi('views/CommonAlertView.ui', self)
        self.__message = message
        self.__setupUiComponents()

    def __keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__acept()

    def __setupUiComponents(self):
        self.content.keyPressEvent = self.__keyPressEvent
        self.message_box.setPlainText(str(self.__message))
        self.btn_accept.clicked.connect(self.__acept)

    def __acept(self):
        self.__application.ui_config_modal("")

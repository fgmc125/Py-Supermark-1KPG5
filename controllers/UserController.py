from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class UserController(QDialog):
    def __init__(self, __application, user):
        super(UserController, self).__init__()
        self.__application = __application
        loadUi('views/UserView.ui', self)
        self.__user = user
        self.__setupUiComponents()

    def __keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__close()

    def __setupUiComponents(self):
        self.tfd_name.setText(self.__user[2])
        self.tfd_surname.setText(self.__user[3])
        self.tfd_email.setText(self.__user[4])
        self.tfd_user.setText(self.__user[1])
        self.tfd_created.setText(str(self.__user[5]))
        self.tfd_updated.setText(str(self.__user[6]))

        self.content.keyPressEvent = self.__keyPressEvent
        self.btn_close.clicked.connect(self.__close)

    def __close(self):
        self.__application.ui_config_modal("")

from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class AlertController(QDialog):
    def __init__(self, __application, id, from_db, message):
        super(AlertController, self).__init__()
        self.__application = __application
        loadUi('views/AlertView.ui', self)
        self.__setupUiComponents()
        self.__id = id
        self.__from = from_db
        self.__message = message

    def __keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__acept()

    def __setupUiComponents(self):
        self.content.keyPressEvent = self.__keyPressEvent
        self.message_box.self.ted_description.setPlainText(self.__message)
        self.btn_acept.clicked.connect(self.__acept)
        self.btn_cancel.clicked.connect(self.__cancel)

    def __acept(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "DELETE FROM "+ self.__from +" WHERE (id = '%s')"
            data = [self.__id]
            self._connector.run_query(query=sql, data=data)
        else:
            print("ALERTA! No se pudo conectar con la base de datos")
        self._connector.close()
        self.__application.load_data()
        self.__application.ui_config_modal("")


    def __cancel(self):
        self.__application.ui_config_modal("")

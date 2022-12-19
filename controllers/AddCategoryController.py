from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class AddCategoryController(QDialog):
    def __init__(self, __application):
        super(AddCategoryController, self).__init__()
        self.__application = __application
        loadUi('views/AddCategoryView.ui', self)
        self.__setupUiComponents()

    def __setupUiComponents(self):
        self.btn_accept.clicked.connect(self.__accept)
        self.btn_accept_and_new.clicked.connect(self.__accept_and_new)
        self.btn_cancel.clicked.connect(self.__cancel)

    def __cancel(self):
        self.__application.ui_config_modal("")

    def __accept_and_new(self):
        if not self.__save():
            self.tfd_name.setText("")
            self.ted_description.setPlainText("")
            self.tfd_image.setText("")

    def __accept(self):
        if not self.__save():
            self.__application.ui_config_modal("")

    def __verify(self):
        return (self.tfd_name.text() != "" and self.ted_description.toPlainText() != "") if True else False

    def __save(self):
        alert = None
        if self.tfd_name.text() != "" and self.ted_description.toPlainText() != "":
            self._connector = Conexion()
            if self._connector.is_connected():
                sql = "SELECT id FROM bhhj3cug6bdknptqdl7k.category_db WHERE name = '" + self.tfd_name.text().title() + "'"
                data = self._connector.run_query(sql)
                if data:
                    self.lbl_info.setStyleSheet("QLabel {\n"
                                                "    font : 77 12px \"Arial\";\n"
                                                "    color : red;"
                                                "}\n")
                    self.lbl_info.setText(" * ¡ERROR! La categoría ingresada ya existe.")
                    alert = " * ¡ERROR! La categoría ingresada ya existe."
                else:
                    sql = """INSERT INTO bhhj3cug6bdknptqdl7k.category_db (
                                                        id,
                                                        name,
                                                        image,
                                                        description
                                                        )
                                                        VALUES (NULL, %s, %s, %s);"""

                    data = self.tfd_name.text().title(), \
                           (self.tfd_image.text()) if self.tfd_image.text() else None, \
                           self.ted_description.toPlainText()

                    self._connector.run_query(query=sql, data=data)
                    self._connector.close()
            else:
                self.lbl_info.setStyleSheet("QLabel {\n"
                                            "    font : 77 12px \"Arial\";\n"
                                            "    color : red;"
                                            "}\n")
                self.lbl_info.setText(" * ¡ERROR! No se pudo realizar la coneccion.")
                alert = " * ¡ERROR! No se pudo realizar la coneccion."
        else:
            self.lbl_info.setStyleSheet("QLabel {\n"
                                        "    font : 77 12px \"Arial\";\n"
                                        "    color : red;"
                                        "}\n")
            self.lbl_info.setText(" * ¡ERROR! Los campos no pueden estar vacios.")
            alert = " * ¡ERROR! Los campos no pueden estar vacios."

        return alert

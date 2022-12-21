from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


from mysqlhelper.Conector import Conexion


class EditCategoryController(QDialog):
    def __init__(self, __application, category):
        super(EditCategoryController, self).__init__()
        self.__application = __application
        loadUi('views/AddCategoryView.ui', self)
        self.__category = category
        self.__setupUiComponents()

    def __setupUiComponents(self):
        self.__load()

        self.tfd_name.setText(str(self.__category[0][1]))
        self.ted_description.setPlainText(self.__category[0][3])
        (self.__category[2]) if self.tfd_image.setText(self.__category[0][2]) else self.tfd_image.setText("")

        self.btn_accept_and_new.deleteLater()
        self.btn_accept.clicked.connect(self.__accept)
        self.btn_cancel.clicked.connect(self.__cancel)

    def __cancel(self):
        self.__application.ui_config_modal("")

    def __accept(self):
        if not self.__save():
            self.__application.ui_config_modal("common_alert", "INFORMACIÓN!, Se modifico correctamente la categoría.")

    def __load(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT * FROM bhhj3cug6bdknptqdl7k.category_db WHERE id = '" + str(self.__category) + "'"
            self.__category = self._connector.run_query(sql)

    def __save(self):
        alert = None
        if self.tfd_name.text() != "" and self.ted_description.toPlainText() != "":
            self._connector = Conexion()
            if self._connector.is_connected():
                if self.tfd_name.text() != self.__category[0][1]:
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
                        sql = "UPDATE bhhj3cug6bdknptqdl7k.category_db  SET name = '" + str(self.tfd_name.text().title())\
                              +"', image = '" + ((self.tfd_image.text()) if self.tfd_image.text() else 'NULL') \
                              + "', description = '" + self.ted_description.toPlainText() \
                              + "' WHERE id = '" + str(self.__category[0][0]) + "'"

                        self._connector.run_query(query=sql)
                        self._connector.close()
                else:
                    sql = "UPDATE bhhj3cug6bdknptqdl7k.category_db  SET name = '" + self.tfd_name.text().title() \
                          + "', image = '" + ((self.tfd_image.text()) if self.tfd_image.text() else None) \
                          + "', description = '" + self.ted_description.toPlainText() \
                          + "' WHERE id = '" + str(self.__category[0][0]) + "'"

                    self._connector.run_query(query=sql)
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

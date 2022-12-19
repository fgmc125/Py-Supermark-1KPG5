from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class EditProductController(QDialog):
    def __init__(self, __application, product):
        super(EditProductController, self).__init__()
        self.__application = __application
        loadUi('views/AddProductView.ui', self)
        self.__setupUiComponents()
        self.__product = product
        self.supplier_data = [("1", "General")]
        self.__load()

    def __setupUiComponents(self):
        self.__load3()

        self.tfd_name.setText(str(self.__category[0][1]))
        self.ted_description.setPlainText(self.__category[0][3])
        (self.__category[2]) if self.tfd_image.setText(self.__category[0][2]) else self.tfd_image.setText("")

        self.btn_accept_and_new.deleteLater()
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
            self.sbx_current.setValue(0)
            self.sbx_min.setValue(0)
            self.sbx_max.setValue(0)
            self.dsb_cost.setValue(0)
            self.dsb_price.setValue(0)
            self.cbx_supplier.setCurrentText(self.supplier_data[0][1])
            self.cbx_category.setCurrentText(self.category_data[0][1])

    def __accept(self):
        if not self.__save():
            self.__application.ui_config_modal("")

    def __load(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT id, name FROM bhhj3cug6bdknptqdl7k.category_db"
            self.category_data = self._connector.run_query(sql)
            if self.category_data:
                for supplier in self.supplier_data:
                    self.cbx_supplier.addItem(supplier[1])
                for category in self.category_data:
                    self.cbx_category.addItem(category[1])
        else:
            self.lbl_info.setStyleSheet("QLabel {\n"
                                        "    font : 77 12px \"Arial\";\n"
                                        "    color : red;"
                                        "}\n")
            self.lbl_info.setText(" * ¡ERROR! No se pudo realizar la coneccion.")

    def __load3(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT * FROM bhhj3cug6bdknptqdl7k.product_db WHERE id = '" + str(self.__product) + "'"
            self.__product = self._connector.run_query(sql)

    def __save(self):
        alert = None
        if self.tfd_name.text() != "" \
                and self.ted_description.toPlainText() != "" \
                and self.sbx_current.value() != 0 \
                and self.dsb_price.value() != 0:
            self._connector = Conexion()
            if self._connector.is_connected():
                sql = "SELECT id FROM bhhj3cug6bdknptqdl7k.product_db WHERE name = '" + self.tfd_name.text().title() + "'"
                data = self._connector.run_query(sql)
                if data:
                    self.lbl_info.setStyleSheet("QLabel {\n"
                                                "    font : 77 12px \"Arial\";\n"
                                                "    color : red;"
                                                "}\n")
                    self.lbl_info.setText(" * ¡ERROR! El producto ingresado ya existe.")
                    alert = " * ¡ERROR! El producto ingresado ya existe."
                else:
                    current_category = None
                    for category in self.category_data:
                        if category[1] == self.cbx_category.currentText():
                            current_category = category[0]
                            break

                    sql = """INSERT INTO bhhj3cug6bdknptqdl7k.product_db (
                                                        id,
                                                        name,
                                                        description,
                                                        price,
                                                        current,
                                                        minimum,
                                                        maximum,
                                                        image,
                                                        created,
                                                        updated,
                                                        new,
                                                        family_id
                                                        )
                                                        VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

                    data = self.tfd_name.text().title(), \
                           self.ted_description.toPlainText(), \
                           self.dsb_price.value(), \
                           self.sbx_current.value(), \
                           self.sbx_min.value(), \
                           self.sbx_max.value(), \
                           (self.tfd_image.text()) if self.tfd_image.text() else None, \
                           datetime.now().strftime('%Y-%m-%d %H:%M:%S'), \
                           datetime.now().strftime('%Y-%m-%d %H:%M:%S'), \
                           True, \
                           current_category

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

    def __save(self):
        alert = None
        print("nombre de la categoria:", self.__product[0][1])
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
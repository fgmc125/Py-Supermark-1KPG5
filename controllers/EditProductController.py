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
        self.__product = product
        self.supplier_data = [("1", "General")]
        self.category_data = None
        self.__load()
        self.__setupUiComponents()

    def __setupUiComponents(self):
        self.__load3()
        print(self.__product)

        self.tfd_name.setText(str(self.__product[0][1]))
        self.ted_description.setPlainText(self.__product[0][2])
        (self.__product[0][7]) if self.tfd_image.setText(self.__product[0][7]) else self.tfd_image.setText("")
        self.sbx_current.setValue(int(self.__product[0][4]))
        self.sbx_min.setValue(int(self.__product[0][5]))
        self.sbx_max.setValue(int(self.__product[0][6]))
        self.dsb_cost.setValue(0)
        self.dsb_price.setValue(float(self.__product[0][3]))
        self.cbx_supplier.setCurrentText(self.supplier_data[0][1])

        current_category = None
        for category in self.category_data:
            if category[0] == self.__product[0][11]:
                current_category = category[1]
                break

        self.cbx_category.setCurrentText(current_category)

        self.btn_accept_and_new.deleteLater()
        self.btn_accept.clicked.connect(self.__accept)
        self.btn_cancel.clicked.connect(self.__cancel)


    def __cancel(self):
        self.__application.ui_config_modal("")

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
                if self.tfd_name.text() != self.__product[0][1]:
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
                        sql = "UPDATE bhhj3cug6bdknptqdl7k.category_db  SET " \
                              "name = '" + str(self.tfd_name.text().title())\
                              + "', image = '" + ((self.tfd_image.text()) if self.tfd_image.text() else 'NULL') \
                              + "', price = '" + str(self.dsb_price.value()) \
                              + "', current = '" + str(self.sbx_current.value()) \
                              + "', minimum = '" + str(self.sbx_min.value()) \
                              + "', maximum = '" + str(self.sbx_max.value()) \
                              + "', updated = '" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') \
                              + "', family_id = '" + str(current_category) \
                              + "', description = '" + self.ted_description.toPlainText() \
                              + "' WHERE id = '" + str(self.__product[0][0]) + "'"

                        self._connector.run_query(query=sql)
                        self._connector.close()
                else:
                    current_category = None
                    for category in self.category_data:
                        if category[1] == self.cbx_category.currentText():
                            current_category = category[0]
                            break
                    sql = "UPDATE bhhj3cug6bdknptqdl7k.category_db  SET " \
                          "name = '" + str(self.tfd_name.text().title()) \
                          + "', image = '" + ((self.tfd_image.text()) if self.tfd_image.text() else 'NULL') \
                          + "', price = '" + str(self.dsb_price.value()) \
                          + "', current = '" + str(self.sbx_current.value()) \
                          + "', minimum = '" + str(self.sbx_min.value()) \
                          + "', maximum = '" + str(self.sbx_max.value()) \
                          + "', updated = '" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') \
                          + "', family_id = '" + str(current_category) \
                          + "', description = '" + self.ted_description.toPlainText() \
                          + "' WHERE id = '" + str(self.__product[0][0]) + "'"

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
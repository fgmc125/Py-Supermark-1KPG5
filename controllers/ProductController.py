from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class ProductController(QtWidgets.QWidget):
    def __init__(self, main_controller, product, category):
        super(ProductController, self).__init__()
        loadUi('views/ProductView.ui', self)
        self.__main_controller = main_controller
        self.__product_data = product
        self.__category = category
        self.__shopping_cart = None
        self.__setupUiComponents()

    def __setupUiComponents(self):
        labels = self.findChildren(QtWidgets.QLabel)
        labels[0].setText(self.__product_data[1])
        labels[1].setText(self.__category)
        self.ted_details.setPlainText(self.__product_data[2])
        self.tfd_price.setText(self.tfd_price.text() + str(self.__product_data[3]))
        self.sbx_amount.setMaximum(int(self.__product_data[4]))
        self.sbx_amount.setValue(1)
        self.sbx_amount.setMinimum(1)

        if self.__main_controller._application.is_staff:
            self.btn_add_to_cart.deleteLater()
            self.btn_buy.deleteLater()
            self.btn_edit.clicked.connect(self.__edit)
            self.btn_remove.clicked.connect(self.__remove)
        else:
            self.btn_add_to_cart.clicked.connect(self.__add_to_cart)
            self.btn_buy.clicked.connect(self.__show_items)
            self.btn_send_message.clicked.connect(self.__show_items)
            self.btn_edit.deleteLater()
            self.btn_remove.deleteLater()


    def __show_items(self):
        pass

    def __remove(self):
        self.__main_controller.ui_config_modal(ui_modal='remove_product', id=self.__product_data[0])
        self.__main_controller._load_content_area_with_categories()

    def __edit(self):
        self.__main_controller.ui_config_modal("edit_product", id=self.__product_data[0])

    def __add_to_cart(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT * FROM bhhj3cug6bdknptqdl7k.shopping_cart_db WHERE product_id = '" + str(self.__product_data[0]) + "'"
            self.__shopping_cart = self._connector.run_query(sql)
            print("Shopping-Cart:", self.__shopping_cart)
            if self.__shopping_cart:
                amount_current = None
                if self.__shopping_cart[0][1] + self.sbx_amount.value() <= self.__product_data[4]:
                    amount_current = self.__shopping_cart[0][1] + self.sbx_amount.value()
                    sql = "UPDATE bhhj3cug6bdknptqdl7k.shopping_cart_db  SET " \
                          "amount = " + str(amount_current) \
                          + ", saved = False" \
                          + " WHERE id = '" + str(self.__shopping_cart[0][0]) + "'"

                    self._connector.run_query(query=sql)
                    self._connector.close()
                    print("Se actualizo tu carrito con exito o sin él, pero se actualizo.")
                else:
                    print("ERROR!, No se puede agregar esa cantidad, solo puedes agregar [", self.sbx_amount.value() - self.__shopping_cart[0][1], "] unidades, porque ya tienes", self.__shopping_cart[0][1], "en el carrito")

            else:
                sql = """INSERT INTO bhhj3cug6bdknptqdl7k.shopping_cart_db (id,amount,saved,product_id,user_id) 
                VALUES (NULL, %s, %s, %s, %s);"""

                data = self.sbx_amount.value(), \
                       False, \
                       self.__product_data[0], \
                       self.__main_controller._application.user_id

                self._connector.run_query(query=sql, data=data)
                self._connector.close()
                print("Se agrgo el producto al carrito.")
        else:
            self.lbl_info.setStyleSheet("QLabel {\n"
                                        "    font : 77 12px \"Arial\";\n"
                                        "    color : red;"
                                        "}\n")
            self.lbl_info.setText(" * ¡ERROR! No se pudo realizar la coneccion.")

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


from mysqlhelper.Conector import Conexion


class AddUserController(QDialog):
    def __init__(self, __application):
        super(AddUserController, self).__init__()
        self.__application = __application
        loadUi('views/AddUserView.ui', self)
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

        if self.tfd_name.text() \
                and self.tfd_surname.text() \
                and self.tfd_user.text() \
                and self.tfd_email.text() \
                and self.tfd_password.text() \
                and self.tfd_repassword.text():
            self._connector = Conexion()
            if self._connector.is_connected():
                sql = "SELECT id FROM bhhj3cug6bdknptqdl7k.user_db WHERE username = '" + self.tfd_user.text() + "'"
                data = self._connector.run_query(sql)
                if data:
                    self.lbl_info.setStyleSheet("QLabel {\n"
                                                "    font : 77 12px \"Arial\";\n"
                                                "    color : red;"
                                                "}\n")
                    alert = " * ¡ERROR! El usuario ingresado ya esta en uso."
                    self.lbl_info.setText(alert)
                else:
                    if self.tfd_password.text() == self.tfd_repassword.text():
                        sql = """INSERT INTO bhhj3cug6bdknptqdl7k.user_db (
                                 id,
                                 password,
                                 last_login,
                                 is_superuser,
                                 username,
                                 first_name,
                                 last_name,
                                 email,
                                 is_staff,
                                 is_active,
                                 date_joined
                                 )
                                 VALUES (NULL, %s, NULL, %s, %s, %s, %s, %s, %s, True, %s);"""

                        data = self.tfd_password.text(), \
                               (self.cbx_is_super_user.isChecked()) if 'True' else 'False', \
                               self.tfd_user.text().lower(), \
                               self.tfd_name.text().title(), \
                               self.tfd_surname.text().title(), \
                               self.tfd_email.text(), \
                               (self.cbx_is_staff.isChecked()) if 'True' else 'False', \
                               datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        self._connector.run_query(query=sql, data=data)
                        self.__application.user = self.tfd_user.text()
                        self._connector.close()
                    else:
                        self.lbl_info.setStyleSheet("QLabel {\n"
                                                    "    font : 77 12px \"Arial\";\n"
                                                    "    color : red;"
                                                    "}\n")
                        alert = " * ¡ERROR! Las contraseñas no coinciden."
                        self.lbl_info.setText(alert)
            else:
                self.lbl_info.setStyleSheet("QLabel {\n"
                                            "    font : 77 12px \"Arial\";\n"
                                            "    color : red;"
                                            "}\n")
                alert = " * ¡ERROR! No se pudo realizar la coneccion."
                self.lbl_info.setText(alert)
        else:
            self.lbl_info.setStyleSheet("QLabel {\n"
                                        "    font : 77 12px \"Arial\";\n"
                                        "    color : red;"
                                        "}\n")
            alert = " * ¡ERROR! Los campos no pueden estar vacios."
            self.lbl_info.setText(alert)

        return alert

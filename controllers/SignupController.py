from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class SignupController(QDialog):
    def __init__(self, __application):
        super(SignupController, self).__init__()
        self.__application = __application
        loadUi('views/SignupView.ui', self)
        self.__setupUiComponents()

    def __keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__signup()

    def __setupUiComponents(self):
        self.content.keyPressEvent = self.__keyPressEvent
        self.btn_cancel.clicked.connect(self.__cancel)
        self.btn_signup.clicked.connect(self.__signup)

    def __cancel(self):
        self.__application.ui_config("login")

    def __signup(self):
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
                    self.lbl_info.setText(" * ¡ERROR! El usuario ingresado ya esta en uso.")
                else:
                    if self.tfd_password.text() == self.tfd_repassword.text():
                        self.lbl_info.setStyleSheet("QLabel {\n"
                                                    "    font : 77 12px \"Arial\";\n"
                                                    "    color : green;"
                                                    "}\n")
                        self.lbl_info.setText(" * ¡CORRECTO! Puede registrarse.")
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
                                VALUES (NULL, %s, NULL, False, %s, %s, %s, %s, False, True, %s);"""

                        data = self.tfd_password.text(), \
                               self.tfd_user.text().lower(), \
                               self.tfd_name.text().title(), \
                               self.tfd_surname.text().title(), \
                               self.tfd_email.text(), \
                               datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        self._connector.run_query(query=sql, data=data)
                        self.__application.user = self.tfd_user.text()
                        self._connector.close()
                        self.__application.ui_config("login")
                    else:
                        self.lbl_info.setStyleSheet("QLabel {\n"
                                                    "    font : 77 12px \"Arial\";\n"
                                                    "    color : red;"
                                                    "}\n")
                        self.lbl_info.setText(" * ¡ERROR! Las contraseñas no coinciden.")
            else:
                self.lbl_info.setStyleSheet("QLabel {\n"
                                            "    font : 77 12px \"Arial\";\n"
                                            "    color : red;"
                                            "}\n")
                self.lbl_info.setText(" * ¡ERROR! No se pudo realizar la coneccion.")
        else:
            self.lbl_info.setStyleSheet("QLabel {\n"
                                        "    font : 77 12px \"Arial\";\n"
                                        "    color : red;"
                                        "}\n")
            self.lbl_info.setText(" * ¡ERROR! Los campos no pueden estar vacios.")

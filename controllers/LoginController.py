from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion


class LoginController(QDialog):
    def __init__(self, __application):
        super(LoginController, self).__init__()
        self.__application = __application
        loadUi('views/LoginView.ui', self)
        self.__setupUiComponents()

        self.tfd_user.setText("user")
        self.tfd_password.setText("123456")

    def __keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__login()

    def __setupUiComponents(self):
        self.content.keyPressEvent = self.__keyPressEvent
        self.btn_login.clicked.connect(self.__login)
        self.btn_signup.clicked.connect(self.__signup)

    def __login(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            if self.tfd_user.text():
                sql = """SELECT password,is_superuser,is_staff,id  FROM bhhj3cug6bdknptqdl7k.user_db WHERE username = %s"""
                data = self.tfd_user.text(),
                sql_return = self._connector.run_query(sql, data)
                if sql_return:
                    if self.tfd_password.text() and sql_return[0][0] == self.tfd_password.text():
                        self.lbl_info.setStyleSheet("QLabel {\n"
                            "    font : 77 12px \"Arial\";\n"
                            "    color : green;"
                            "}\n")
                        self.lbl_info.setText(" * ¡CORRECTO! Puso bien los datos.")
                        sql = """UPDATE bhhj3cug6bdknptqdl7k.user_db SET last_login = %s WHERE username = %s"""
                        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.tfd_user.text()
                        self._connector.run_query(sql, data)
                        self.__application.user = self.tfd_user.text()
                        self.__application.is_superuser = (sql_return[0][1] == 1) if True else False
                        self.__application.is_staff = (sql_return[0][2] == 1) if True else False
                        self.__application.user_id = sql_return[0][3]
                        self._connector.close()
                        self.__application.ui_config("main")
                    else:
                        self.lbl_info.setStyleSheet(
                            "QLabel {\n"
                            "    font : 77 12px \"Arial\";\n"
                            "    color : red;"
                            "}\n"
                        )
                        self.lbl_info.setText(" * ¡ERROR! Contraseña incorrecta.")
                else:
                    self.lbl_info.setStyleSheet(
                        "QLabel {\n"
                        "    font : 77 12px \"Arial\";\n"
                        "    color : red;"
                        "}\n"
                    )
                    self.lbl_info.setText(
                        " * ¡ERROR! El usuario [ " + self.tfd_user.text() + " ] no esta registrado.")
            else:
                self.lbl_info.setStyleSheet(
                    "QLabel {\n"
                    "    font : 77 12px \"Arial\";\n"
                    "    color : red;"
                    "}\n"
                )
                self.lbl_info.setText(" * ¡ERROR! Los campos no pueden estar vacios.")
        else:
            self.lbl_info.setStyleSheet(
                "QLabel {\n"
                "    font : 77 12px \"Arial\";\n"
                "    color : red;"
                "}\n"
            )
            self.lbl_info.setText(" * ¡ERROR! No se pudo realizar la coneccion.")

        self._connector.close()

    def __signup(self):
        self.__application.ui_config("signup")

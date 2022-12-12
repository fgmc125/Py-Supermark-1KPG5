import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from mysqlhelper.Conector import Conexion

from controllers.MainWindow import UiMainWindow


class LoginController(QDialog):
    def __init__(self,__application):
        super(LoginController, self).__init__()
        self.__application = __application
        loadUi('views/LoginView.ui', self)
        self.__setupUiComponents()

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
                data = self._connector.run_query(
                    "SELECT contrasenia FROM byesikch2cyefw2pvcqg.usuario WHERE id = '" + self.tfd_user.text() + "'")
                if data:
                    if self.tfd_password.text() and data[0][0] == self.tfd_password.text():
                        self.lbl_info.setStyleSheet(
                            "QLabel {\n"
                            "    font : 77 12px \"Arial\";\n"
                            "    color : green;"
                            "}\n"
                        )
                        self.lbl_info.setText(" * ¡CORRECTO! Puso bien los datos.")
                        date_time = str(datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
                        sql = "UPDATE `byesikch2cyefw2pvcqg`.`usuario`" \
                              " SET `fecha_acceso` = '" + date_time + "' WHERE (`id` = '" + self.tfd_user.text() + "');"
                        self._connector.run_query(sql)
                        self.__application.user = self.tfd_user.text()
                        self._connector.close()
                        #self.__application.ui_config(QtWidgets.QMainWindow(), UiMainWindow(self.__application, self))
                        self.__application.ui_config_without_qwidget("main")
                    else:
                        self.lbl_info.setStyleSheet("")
                        self.lbl_info.setText(" * ¡ERROR! Contraseña incorrecta.")
                else:
                    self.lbl_info.setStyleSheet("")
                    self.lbl_info.setText(
                        " * ¡ERROR! El usuario [ " + self.tfd_user.text() + " ] no esta registrado.")
            else:
                self.lbl_info.setStyleSheet("")
                self.lbl_info.setText(" * ¡ERROR! Los campos no pueden estar vacios.")
        else:
            self.lbl_info.setStyleSheet("")
            self.lbl_info.setText(" * ¡ERROR! No se pudo realizar la coneccion.")

        self._connector.close()

    def __signup(self):
        self.__application.ui_config_without_qwidget("signup")

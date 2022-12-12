import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

from mysqlhelper.Conector import Conexion
from controllers.Signup import UiDialogSignup
from controllers.MainWindow import UiMainWindow

class UiDialogLogin(object):
    def __init__(self, __application):
        self.__application = __application

    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(405, 310)
        dialog.setStyleSheet("QDialog {\n"
                             "    background-color : #FFF;\n"
                             "    margin : 0px;\n"
                             "    padding : 0px;\n"
                             "}\n"
                             "\n"
                             "QFrame#content {\n"
                             "    background-color : transparent;\n"
                             "    border: 1px solid #DADDE1;\n"
                             "    border-radius: 5px;\n"
                             "    min-width : 380px;\n"
                             "    min-height : 285px;\n"
                             "}\n"
                             "\n"
                             "QLabel {\n"
                             "    font : 77 12px \"Arial\";\n"
                             "    color : red;\n"
                             "}\n"
                             "\n"
                             "QLineEdit {\n"
                             "    background-color : transparent;\n"
                             "    border : 1px solid #DADDE1;\n"
                             "    border-radius : 5px;\n"
                             "    color : #616161;\n"
                             "    min-height : 40px;\n"
                             "    font : 77 18px \"Arial\";\n"
                             "}\n"
                             "\n"
                             "QPushButton {\n"
                             "    color : #FFFFFF;\n"
                             "    border-style : solid;\n"
                             "    border-radius: 5px;\n"
                             "    min-height : 40px;\n"
                             "    font : 77 18px \"Arial\";\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_login {\n"
                             "    background-color : #1877F2;\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_login:pressed {\n"
                             "    background-color : transparent;\n"
                             "    color : #1877F2;\n"
                             "    border: 1px solid #1877F2;\n"
                             "    border-radius: 5px;\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_signup {\n"
                             "    background-color : #42B72A;\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_signup:hover, #btn_exit:hover, #btn_login:hover {\n"
                             "    border: 1px solid #FFF;\n"
                             "    border-radius: 5px;\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_signup:pressed {\n"
                             "    background-color : transparent;\n"
                             "    color : #42B72A;\n"
                             "    border: 1px solid #42B72A;\n"
                             "    border-radius: 5px;\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_exit {\n"
                             "    background-color : #616161;\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_exit:pressed {\n"
                             "    background-color : transparent;\n"
                             "    color : #616161;\n"
                             "    border: 1px solid #616161;\n"
                             "    border-radius: 5px;\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_forgotten_password {\n"
                             "    border-style: outset;\n"
                             "    border-width: 0px;\n"
                             "    color : #1877F2;\n"
                             "    font : 77 15px \"Arial\";\n"
                             "}\n"
                             "\n"
                             "QPushButton#btn_forgotten_password:hover {\n"
                             "    text-decoration: underline;\n"
                             "}")

        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.content = QtWidgets.QFrame(dialog)
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lbl_info = QtWidgets.QLabel(self.content)
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_info.setStyleSheet("QLabel {\n"
                                    "    font : 77 12px \"Arial\";\n"
                                    "    color : green;"
                                    "}\n")
        self.verticalLayout_2.addWidget(self.lbl_info)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tfd_user = QtWidgets.QLineEdit(self.content)
        self.tfd_user.setObjectName("tfd_user")
        self.verticalLayout_2.addWidget(self.tfd_user)
        self.tfd_password = QtWidgets.QLineEdit(self.content)
        self.tfd_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tfd_password.setObjectName("tfd_password")
        self.verticalLayout_2.addWidget(self.tfd_password)
        self.btn_forgotten_password = QtWidgets.QPushButton(self.content)
        self.btn_forgotten_password.setObjectName("btn_forgotten_password")
        self.verticalLayout_2.addWidget(self.btn_forgotten_password)
        self.btn_login = QtWidgets.QPushButton(self.content)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout_2.addWidget(self.btn_login)
        self.btn_signup = QtWidgets.QPushButton(self.content)
        self.btn_signup.setObjectName("btn_signup")
        self.verticalLayout_2.addWidget(self.btn_signup)
        self.verticalLayout.addWidget(self.content)

        self.__setupUiComponents()

        self.__retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def __retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.lbl_info.setText(_translate("Dialog", " * Ingrese sus datos de inicio de sesión."))
        self.tfd_user.setPlaceholderText(_translate("Dialog", " Ingrese su usuario"))
        self.tfd_password.setPlaceholderText(_translate("Dialog", " Ingrese su contraseña"))
        self.btn_forgotten_password.setText(_translate("Dialog", "¿Olvidaste tu contraseña?"))
        self.btn_login.setText(_translate("Dialog", "Iniciar sesión"))
        self.btn_signup.setText(_translate("Dialog", "Crear cuenta"))

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
                        self.__application.ui_config(QtWidgets.QMainWindow(), UiMainWindow(self.__application, self))
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
        self.__application.ui_config(QDialog(), UiDialogSignup(self.__application, self))

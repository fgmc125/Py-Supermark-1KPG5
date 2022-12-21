from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


from mysqlhelper.Conector import Conexion


class EditUserController(QDialog):
    def __init__(self, __application, user):
        super(EditUserController, self).__init__()
        self.__application = __application
        loadUi('views/AddUserView.ui', self)
        self.__user = user
        self.__setupUiComponents()

    def __setupUiComponents(self):
        if self.__user[1] == "user" or self.__user[1] == "admin":
            self.tfd_user.setReadOnly(True)
            self.tfd_user.setEnabled(False)
        self.tfd_name.setText(self.__user[2])
        self.tfd_surname.setText(self.__user[3])
        self.tfd_email.setText(self.__user[4])
        self.tfd_user.setText(self.__user[1])
        self.tfd_password.setText("")
        self.tfd_repassword.setText("") #if password is blank skip
        self.cbx_is_super_user.setChecked((self.__user[7] == 1) if True else False)
        self.cbx_is_staff.setChecked((self.__user[8] == 1) if True else False)

        self.btn_accept.clicked.connect(self.__accept)
        self.btn_accept_and_new.deleteLater()
        self.btn_cancel.clicked.connect(self.__cancel)

    def __cancel(self):
        self.__application.ui_config_modal("")

    def __accept(self):
        if not self.__save():
            self.__application.ui_config_modal("common_alert", "INFORMACIÓN!, Se modifico correctamente el usuario.")

    def __verify(self):
        return (self.tfd_name.text() != "" and self.ted_description.toPlainText() != "") if True else False

    def __save(self):
        alert = None

        if self.tfd_name.text() \
                and self.tfd_surname.text() \
                and self.tfd_user.text() \
                and self.tfd_email.text():

            self._connector = Conexion()
            if self._connector.is_connected():
                if self.tfd_user.text() != self.tfd_user.text():
                    sql = "SELECT id FROM bhhj3cug6bdknptqdl7k.user_db WHERE username = '" + self.tfd_user.text().lower() + "'"
                    data = self._connector.run_query(sql)
                    if data:
                        self.lbl_info.setStyleSheet("QLabel {\n"
                                                    "    font : 77 12px \"Arial\";\n"
                                                    "    color : red;"
                                                    "}\n")
                        alert = " * ¡ERROR! El usuario ingresado ya esta en uso."
                        self.lbl_info.setText(alert)
                    else:
                        if self.tfd_password.text() and self.tfd_repassword.text():
                            if self.tfd_password.text() == self.tfd_repassword.text():
                                sql = "UPDATE bhhj3cug6bdknptqdl7k.user_db  SET " \
                                      "password = '" + self.tfd_password.text() \
                                      + "', is_superuser = " + (
                                      self.cbx_is_super_user.isChecked()) if 'True' else 'False' \
                                      + ", username = '" + self.tfd_user.text().lower() \
                                      + "', first_name = '" + self.tfd_name.text().title() \
                                      + "', last_name = '" + str(self.tfd_surname.text().title()) \
                                      + "', email = '" + self.tfd_email.text() \
                                      + "', is_staff = " + (self.cbx_is_staff.isChecked()) if 'True' else 'False' \
                                      + " WHERE id = '" + str(self.__user[0]) + "'"

                                self._connector.run_query(query=sql)
                                self._connector.close()
                            else:
                                self.lbl_info.setStyleSheet("QLabel {\n"
                                                            "    font : 77 12px \"Arial\";\n"
                                                            "    color : red;"
                                                            "}\n")
                                alert = " * ¡ERROR! Las contraseñas no coinciden."
                                self.lbl_info.setText(alert)
                        else:
                            sql = "UPDATE bhhj3cug6bdknptqdl7k.user_db  SET " \
                                  "is_superuser = '" + ((self.cbx_is_super_user.isChecked()) if 'True' else 'False') \
                                  + "', username = '" + self.tfd_user.text().lower() \
                                  + "', first_name = '" + self.tfd_name.text().title() \
                                  + "', last_name = '" + str(self.tfd_surname.text().title()) \
                                  + "', email = '" + self.tfd_email.text() \
                                  + "', is_staff = " + ((self.cbx_is_staff.isChecked()) if 'True' else 'False') \
                                  + " WHERE id = '" + str(self.__user[0]) + "'"

                            self._connector.run_query(query=sql)
                            self._connector.close()
                else:
                    if self.tfd_password.text() and self.tfd_repassword.text():
                        if self.tfd_password.text() == self.tfd_repassword.text():
                            sql = "UPDATE bhhj3cug6bdknptqdl7k.user_db  SET " \
                                  "password = '" + self.tfd_password.text() \
                                  + "', is_superuser = " + (self.cbx_is_super_user.isChecked()) if 'True' else 'False' \
                                  + ", first_name = '" + self.tfd_name.text().title() \
                                  + "', last_name = '" + str(self.tfd_surname.text().title()) \
                                  + "', email = '" + self.tfd_email.text() \
                                  + "', is_staff = " + (self.cbx_is_staff.isChecked()) if 'True' else 'False' \
                                  + " WHERE id = '" + str(self.__user[0]) + "'"

                            self._connector.run_query(query=sql)
                            self._connector.close()
                        else:
                            self.lbl_info.setStyleSheet("QLabel {\n"
                                                        "    font : 77 12px \"Arial\";\n"
                                                        "    color : red;"
                                                        "}\n")
                            alert = " * ¡ERROR! Las contraseñas no coinciden."
                            self.lbl_info.setText(alert)
                    else:
                        sql = "UPDATE bhhj3cug6bdknptqdl7k.user_db  SET " \
                              "is_superuser = " + str((self.cbx_is_super_user.isChecked()) if 'True' else 'False') \
                              + ", first_name = '" + self.tfd_name.text().title() \
                              + "', last_name = '" + str(self.tfd_surname.text().title()) \
                              + "', email = '" + self.tfd_email.text() \
                              + "', is_staff = " + str((self.cbx_is_staff.isChecked()) if 'True' else 'False') \
                              + " WHERE id = '" + str(self.__user[0]) + "'"

                        self._connector.run_query(query=sql)
                        self._connector.close()
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

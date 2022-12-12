from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QSpacerItem, QTableWidgetItem

from mysqlhelper.Conector import Conexion
from mysqlhelper.MySQLHelper import MySQLHelper


class UiMainWindow(object):
    def __init__(self, __application, __login):
        self.__mysql_helper = MySQLHelper()
        self.__login = __login
        self.__application = __application

    def setupUi(self, mainWindow):
        self.main_windows = mainWindow
        self.main_windows.setObjectName("MainWindow")
        self.main_windows.resize(524, 567)
        self.main_windows.setStyleSheet("QMainWindow {\n"
                                        "    background-color : #FFF;\n"
                                        "    margin : 0px;\n"
                                        "    padding : 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QFrame {\n"
                                        "    margin : 0px;\n"
                                        "    padding : 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QFrame#fme_header {\n"
                                        "    min-height : 74px;\n"
                                        "    margin : 0px;\n"
                                        "    padding : 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QFrame#fme_primary_buttons, #fme_secondary_buttons {\n"
                                        "    min-height : 34px;\n"
                                        "    margin : 0px;\n"
                                        "    padding : 0px;\n"
                                        "}\n"
                                        "\n"
                                        "QFrame#fme_primary_buttons {\n"
                                        "    background-color : #42B72A;\n"
                                        "}\n"
                                        "\n"
                                        "QFrame#fme_secondary_buttons, #fme_header {\n"
                                        "    background-color : #1877F2;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "    font : 77 16px \"Arial\";\n"
                                        "    color : #FFFFFF;\n"
                                        "    border-style : solid;\n"
                                        "    border-radius: 5px;\n"
                                        "    transition: 0.9s;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#btn_logout {\n"
                                        "    font : 77 8pt \"Arial\";\n"
                                        "    transition: 0.9s;\n"
                                        "    background-color : #42B72A;\n"
                                        "    min-width : 90px;\n"
                                        "    min-height : 28px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#btn_logout:pressed {\n"
                                        "    background-color : transparent;\n"
                                        "    color : #42B72A;\n"
                                        "    border: 1px solid #42B72A;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#btn_profile {\n"
                                        "    background-color : transparent;\n"
                                        "    min-width : 50px;\n"
                                        "    min-height : 50px;\n"
                                        "    max-width : 50px;\n"
                                        "    max-height : 50px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 1px solid #FFF;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QLabel {\n"
                                        "    color : #FFF;\n"
                                        "    font : 77 16pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QLabel#lbl_title {\n"
                                        "    color : #000;\n"
                                        "    font : 77 16pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QLabel#lbl_aux0, #lbl_aux1 {\n"
                                        "    color : #000;\n"
                                        "    font : 77 8pt \"Arial\";\n"
                                        "}"
                                        "QTableView {\n"
                                        "    background-color: transparent;\n"
                                        "    font-size:13px;\n"
                                        "}\n"
                                        "\n"
                                        "QHeaderView::section:horizontal {\n"
                                        "    color: #fff;\n"
                                        "    border-style: solid;\n"
                                        "    background-color: #1877F2;\n"
                                        " }\n"
                                        "\n"
                                        "QTableWidget {\n"
                                        "    border: 2px solid #1877F2;\n"
                                        "    border-top-color: #1877F2;\n"
                                        "    gridline-color: #1877F2;\n"
                                        "    selection-background-color: #B5DDD6;\n"
                                        "    color:#333;\n"
                                        "    font-size:12px;\n"
                                        " }")

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fme_header = QtWidgets.QFrame(self.centralwidget)
        self.fme_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_header.setObjectName("fme_header")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fme_header)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_profile = QtWidgets.QPushButton(self.fme_header)
        self.btn_profile.setText("")
        self.btn_profile.setObjectName("btn_profile")
        self.horizontalLayout_5.addWidget(self.btn_profile)
        self.label_4 = QtWidgets.QLabel(self.fme_header)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btn_logout = QtWidgets.QPushButton(self.fme_header)
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout_5.addWidget(self.btn_logout)
        self.verticalLayout.addWidget(self.fme_header)
        self.fme_top = QtWidgets.QFrame(self.centralwidget)
        self.fme_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_top.setObjectName("fme_top")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fme_top)
        self.horizontalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_title = QtWidgets.QLabel(self.fme_top)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayout_4.addWidget(self.lbl_title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.fme_top)
        self.fme_center = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fme_center.sizePolicy().hasHeightForWidth())
        self.fme_center.setSizePolicy(sizePolicy)
        self.fme_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_center.setObjectName("fme_center")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fme_center)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spacerItem2 = QtWidgets.QSpacerItem(20, 340, QtWidgets.QSizePolicy.Minimum,
                                                 QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem2)
        self.verticalLayout.addWidget(self.fme_center)
        self.fme_bottom = QtWidgets.QFrame(self.centralwidget)
        self.fme_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_bottom.setObjectName("fme_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fme_bottom)
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_aux0 = QtWidgets.QLabel(self.fme_bottom)
        self.lbl_aux0.setText("")
        self.lbl_aux0.setObjectName("lbl_aux0")
        self.horizontalLayout.addWidget(self.lbl_aux0)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lbl_aux1 = QtWidgets.QLabel(self.fme_bottom)
        self.lbl_aux1.setText("")
        self.lbl_aux1.setObjectName("lbl_aux1")
        self.horizontalLayout.addWidget(self.lbl_aux1)
        self.verticalLayout.addWidget(self.fme_bottom)

        self.fme_secondary_buttons = QtWidgets.QFrame(self.centralwidget)
        self.fme_secondary_buttons.setStyleSheet("QPushButton {\n"
                                                 "    color : #FFFFFF;\n"
                                                 "    border-style : solid;\n"
                                                 "    border-radius: 5px;\n"
                                                 "    min-height : 34px;\n"
                                                 "    min-width : 166px;\n"
                                                 "    transition: 0.9s;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "    background-color : transparent;\n"
                                                 "    border-style: outset;\n"
                                                 "    border-width: 0px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color : #FFF;\n"
                                                 "    color : #1877F2;\n"
                                                 "    border-style : none;\n"
                                                 "    border-radius: 0px;\n"
                                                 "}")
        self.fme_secondary_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_secondary_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_secondary_buttons.setObjectName("fme_secondary_buttons")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fme_secondary_buttons)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        btn = QtWidgets.QPushButton(self.fme_secondary_buttons)
        btn.setObjectName("btn_show_users")
        self.horizontalLayout_3.addWidget(btn)

        self.verticalLayout.addWidget(self.fme_secondary_buttons)

        #self.btn_show_users = QtWidgets.QPushButton(self.fme_secondary_buttons)
        #self.btn_show_users.setObjectName("btn_show_users")
        #self.horizontalLayout_3.addWidget(self.btn_show_users)
        #self.verticalLayout.addWidget(self.fme_secondary_buttons)

        self.fme_primary_buttons = QtWidgets.QFrame(self.centralwidget)
        self.fme_primary_buttons.setStyleSheet("QPushButton {\n"
                                               "    color : #FFFFFF;\n"
                                               "    border-style : solid;\n"
                                               "    border-radius: 5px;\n"
                                               "    transition: 0.9s;\n"
                                               "    min-width : 166px;\n"
                                               "    min-height : 34px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color : transparent;\n"
                                               "    border-style: outset;\n"
                                               "    border-width: 0px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color : #FFF;\n"
                                               "    color : #42B72A;\n"
                                               "    border-style : none;\n"
                                               "    border-radius: 0px;\n"
                                               "}")
        self.fme_primary_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_primary_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_primary_buttons.setObjectName("fme_primary_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fme_primary_buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_show_students = QtWidgets.QPushButton(self.fme_primary_buttons)
        self.btn_show_students.setObjectName("btn_show_student")
        self.horizontalLayout_2.addWidget(self.btn_show_students)
        self.verticalLayout.addWidget(self.fme_primary_buttons)
        mainWindow.setCentralWidget(self.centralwidget)

        self.__setupUiComponents()

        self.retranslateUi(self.main_windows)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", self.__application.user))
        self.btn_logout.setText(_translate("MainWindow", "Cerrar sesión"))
        self.lbl_title.setText(_translate("MainWindow", "Inicio"))
        self.fme_secondary_buttons.findChild(QtWidgets.QPushButton, "btn_show_users").setText(_translate("MainWindow", "Ver usuarios"))
        self.fme_primary_buttons.findChild(QtWidgets.QPushButton, "btn_show_student").setText(_translate("MainWindow", "Ver estudiantes"))

    def __setupUiComponents(self):
        self.btn_logout.clicked.connect(self.__logout)
        self.fme_secondary_buttons.findChild(QtWidgets.QPushButton, "btn_show_users").clicked.connect(self.__show_users)
        self.fme_primary_buttons.findChild(QtWidgets.QPushButton, "btn_show_student").clicked.connect(self.__show_students)

    def __logout(self):
        self.__application.ui_config(QDialog(), self.__login)

    def __show_students(self):
        self.__clean()

        self.btn_show_students.clicked.disconnect(self.__show_students)
        self.btn_show_students.clicked.connect(self.__back)
        self.btn_show_students.setText("Volver")
        self.lbl_title.setText("Estudiantes")

        self.__qtable(header=["ID",
                  "COHORTE",
                  "COND. CURSADO",
                  "COND. ESTUDIANTE",
                  "ESTADO TPF",
                  "FECHA DE ALTA",
                  "RESPNSABLE ALTA",
                  "FECHA DE MODIFICACION",
                  "RESPNSABLE MODIFICACION",
                  "P1",
                  "RP1",
                  "P2",
                  "RP2"],
                      data=self.__mysql_helper.student_list())

    def __show_users(self):
        self.__clean()
        self.__qtable(header=["ID", "NOMBRE", "APELLIDO", "TIPO", "CORREO", "ULTIMA CONECCION","ADMITIDO"],
                      data=self.__mysql_helper.user_list())

        self.__fme_buttons_config(items_object=["btn_back", "btn_delete", "btn_modificar"],
                                  items_name=["Volver", "Eliminar", "Modifiacar"],
                                  clean="QPushButton_Secondary")

    def __fme_buttons_config(self, clean, items_object, items_name):
        self.__clean(clean)
        _translate = QtCore.QCoreApplication.translate

        for i in range(len(items_object)):
            btn = QtWidgets.QPushButton(self.fme_secondary_buttons)
            btn.setObjectName(items_object[i])
            btn.setText(_translate("MainWindow", items_name[i]))
            self.horizontalLayout_3.addWidget(btn)
        pass

    def __qtable(self, header, data):
        _translate = QtCore.QCoreApplication.translate

        self.tableWidget = QtWidgets.QTableWidget(self.fme_center)
        self.tableWidget.setGeometry(QtCore.QRect(130, 150, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.spacerItem2.changeSize(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)

        self.tableWidget.setEnabled(True)
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setObjectName("tableWidget")

        for i in range(len(header)):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.tableWidget.setSortingEnabled(True)

        for i in range(len(header)):
            self.tableWidget.horizontalHeaderItem(i).setText(_translate("MainWindow", header[i]))

        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def __back(self):
        self.__clean()
        self.btn_show_users.clicked.disconnect(self.__back)
        self.btn_show_users.clicked.connect(self.__show_users)
        self.btn_show_users.setText("Ver usuarios")
        self.lbl_title.setText("Inicio")

    def __clean(self, name="QTableWidget"):
        if name == "QTableWidget":
            data = self.fme_center.findChild(QtWidgets.QTableWidget)
            if data:
                self.spacerItem2.changeSize(20, 340, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                data.deleteLater()
        elif name == "QPushButton_Primary":
            data = self.fme_primary_buttons.findChildren(QtWidgets.QPushButton)
            for qwidget in data:
                qwidget.deleteLater()
            data = self.fme_primary_buttons.findChild(QSpacerItem)
            if data: data.deleteLater()
        elif name == "QPushButton_Secondary":
            data = self.fme_secondary_buttons.findChildren(QtWidgets.QPushButton)
            for qwidget in data:
                qwidget.deleteLater()
            data = self.fme_primary_buttons.findChild(QSpacerItem)
            if data: data.deleteLater()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

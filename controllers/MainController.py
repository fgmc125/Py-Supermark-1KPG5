from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from views.assets import *


class MainController(QMainWindow):
    def __init__(self,__application):
        super(MainController, self).__init__()
        self.__application = __application
        loadUi('views/MainView.ui', self)
        self.__setupUiComponents()

    def __setupUiComponents(self):
        pass
    # def __setupUiComponents(self):
    #     self.btn_logout.clicked.connect(self.__logout)
    #     self.fme_secondary_buttons.findChild(QtWidgets.QPushButton, "btn_show_users").clicked.connect(self.__show_users)
    #     self.fme_primary_buttons.findChild(QtWidgets.QPushButton, "btn_show_student").clicked.connect(self.__show_students)
    #
    # def __logout(self):
    #     self.__application.ui_config(QDialog(), self.__login)
    #
    # def __show_students(self):
    #     self.__clean()
    #
    #     self.btn_show_students.clicked.disconnect(self.__show_students)
    #     self.btn_show_students.clicked.connect(self.__back)
    #     self.btn_show_students.setText("Volver")
    #     self.lbl_title.setText("Estudiantes")
    #
    #     self.__qtable(header=["ID",
    #               "COHORTE",
    #               "COND. CURSADO",
    #               "COND. ESTUDIANTE",
    #               "ESTADO TPF",
    #               "FECHA DE ALTA",
    #               "RESPNSABLE ALTA",
    #               "FECHA DE MODIFICACION",
    #               "RESPNSABLE MODIFICACION",
    #               "P1",
    #               "RP1",
    #               "P2",
    #               "RP2"],
    #                   data=self.__mysql_helper.student_list())
    #
    # def __show_users(self):
    #     self.__clean()
    #     self.__qtable(header=["ID", "NOMBRE", "APELLIDO", "TIPO", "CORREO", "ULTIMA CONECCION","ADMITIDO"],
    #                   data=self.__mysql_helper.user_list())
    #
    #     self.__fme_buttons_config(items_object=["btn_back", "btn_delete", "btn_modificar"],
    #                               items_name=["Volver", "Eliminar", "Modifiacar"],
    #                               clean="QPushButton_Secondary")
    #
    # def __fme_buttons_config(self, clean, items_object, items_name):
    #     self.__clean(clean)
    #     _translate = QtCore.QCoreApplication.translate
    #
    #     for i in range(len(items_object)):
    #         btn = QtWidgets.QPushButton(self.fme_secondary_buttons)
    #         btn.setObjectName(items_object[i])
    #         btn.setText(_translate("MainWindow", items_name[i]))
    #         self.horizontalLayout_3.addWidget(btn)
    #     pass
    #
    # def __qtable(self, header, data):
    #     _translate = QtCore.QCoreApplication.translate
    #
    #     self.tableWidget = QtWidgets.QTableWidget(self.fme_center)
    #     self.tableWidget.setGeometry(QtCore.QRect(130, 150, 256, 192))
    #     self.tableWidget.setObjectName("tableWidget")
    #     self.verticalLayout_2.addWidget(self.tableWidget)
    #     self.spacerItem2.changeSize(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
    #
    #     self.tableWidget.setEnabled(True)
    #     self.tableWidget.setAcceptDrops(True)
    #     self.tableWidget.setAutoFillBackground(True)
    #     self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
    #     self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
    #     self.tableWidget.setLineWidth(1)
    #     self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
    #     self.tableWidget.setDragEnabled(True)
    #     self.tableWidget.setAlternatingRowColors(True)
    #     self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    #     self.tableWidget.setShowGrid(True)
    #     self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
    #     self.tableWidget.setCornerButtonEnabled(True)
    #     self.tableWidget.setRowCount(0)
    #     self.tableWidget.setColumnCount(len(header))
    #     self.tableWidget.setObjectName("tableWidget")
    #
    #     for i in range(len(header)):
    #         self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())
    #
    #     self.tableWidget.horizontalHeader().setVisible(True)
    #     self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
    #     self.tableWidget.horizontalHeader().setHighlightSections(False)
    #     self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
    #     self.tableWidget.horizontalHeader().setStretchLastSection(True)
    #     self.tableWidget.verticalHeader().setVisible(False)
    #     self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
    #     self.tableWidget.verticalHeader().setHighlightSections(True)
    #     self.tableWidget.verticalHeader().setSortIndicatorShown(False)
    #     self.tableWidget.verticalHeader().setStretchLastSection(False)
    #
    #     self.tableWidget.setSortingEnabled(True)
    #
    #     for i in range(len(header)):
    #         self.tableWidget.horizontalHeaderItem(i).setText(_translate("MainWindow", header[i]))
    #
    #     self.tableWidget.setRowCount(len(data))
    #     for i in range(len(data)):
    #         for j in range(len(data[i])):
    #             self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
    #
    # def __back(self):
    #     self.__clean()
    #     self.btn_show_users.clicked.disconnect(self.__back)
    #     self.btn_show_users.clicked.connect(self.__show_users)
    #     self.btn_show_users.setText("Ver usuarios")
    #     self.lbl_title.setText("Inicio")
    #
    # def __clean(self, name="QTableWidget"):
    #     if name == "QTableWidget":
    #         data = self.fme_center.findChild(QtWidgets.QTableWidget)
    #         if data:
    #             self.spacerItem2.changeSize(20, 340, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    #             data.deleteLater()
    #     elif name == "QPushButton_Primary":
    #         data = self.fme_primary_buttons.findChildren(QtWidgets.QPushButton)
    #         for qwidget in data:
    #             qwidget.deleteLater()
    #         data = self.fme_primary_buttons.findChild(QSpacerItem)
    #         if data: data.deleteLater()
    #     elif name == "QPushButton_Secondary":
    #         data = self.fme_secondary_buttons.findChildren(QtWidgets.QPushButton)
    #         for qwidget in data:
    #             qwidget.deleteLater()
    #         data = self.fme_primary_buttons.findChild(QSpacerItem)
    #         if data: data.deleteLater()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from controllers.CardController import CardController
from mysqlhelper.Conector import Conexion
from views.assets import *


class MainController(QMainWindow):
    def __init__(self, __application):
        super(MainController, self).__init__()
        self.__application = __application
        loadUi('views/MainView.ui', self)
        self.__setupUiComponents()
        self.__isToggler = True
        self._connector = None
        self.category_data = None

    def __setupUiComponents(self):
        if self.__application.is_staff:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icon/assets/icon/users.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_1.setIcon(icon)
            self.btn_1.setToolTip("Ver usuarios")
            self.btn_1_stylesheet = "#fme_lbl_title { background-image : url(:/icon/assets/icon/users2.png);}"
            self.btn_1_title = " USUARIOS"
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icon/assets/icon/cart-shopping.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn_1.setIcon(icon)
            self.btn_1.setToolTip("Mostrar mi carrito")
            self.btn_1_stylesheet = "#fme_lbl_title { background-image : url(:/icon/assets/icon/cart-shopping2.png);}"
            self.btn_1_title = " MI CARRITO"

        self.btn_username.setText(self.__application.user)

        self.lbl_version.setText(self.__application.getTitle())
        self.btn_toggler.clicked.connect(self.__toggler_action)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_0").clicked.connect(self.__show_home)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_1").clicked.connect(self.__action_button_1)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_2").clicked.connect(self.__show_categories)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_exit").clicked.connect(self.__logout)

    def __toggler_action(self):
        if self.__isToggler:
            self.fme_aside.setMaximumWidth(130)
            self.fme_aside.setMinimumWidth(130)
            self.btn_toggler.setText(" Menú")
            self.btn_0.setText(" Inicio")
            self.btn_1.setText(" Perfil")
            self.btn_2.setText(" Categorías")
            self.btn_exit.setText(" Opciones")
            self.__isToggler = False
        else:
            self.fme_aside.setMaximumWidth(51)
            self.fme_aside.setMinimumWidth(51)
            self.btn_toggler.setText("")
            self.btn_0.setText("")
            self.btn_1.setText("")
            self.btn_2.setText("")
            self.btn_exit.setText("")
            self.__isToggler = True

    def __action_button_1(self):
        self.fme_lbl_title.setStyleSheet(self.btn_1_stylesheet)
        self.lbl_title.setText(self.btn_1_title)

    def __show_home(self):
        self.__clean()
        self.fme_lbl_title.setStyleSheet("#fme_lbl_title { background-image : url(:/icon/assets/icon/house2.png);}")
        self.lbl_title.setText(" INICIO")

    def __show_categories(self):
        _translate = QtCore.QCoreApplication.translate
        if self.__application.is_staff:
            self.__clean()
            self.btn_item_var_1 = QtWidgets.QPushButton(self.frame_3)
            self.btn_item_var_1.setObjectName("btn_item_var_1")
            self.horizontalLayout_10.addWidget(self.btn_item_var_1)
            self.btn_item_var_1.setText(_translate("MainWindow", "Nueva categoría"))
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_1").clicked.connect(self.new_category)

            self.btn_item_var_0 = QtWidgets.QPushButton(self.frame_3)
            self.btn_item_var_0.setObjectName("btn_item_var_0")
            self.horizontalLayout_10.addWidget(self.btn_item_var_0)
            self.btn_item_var_0.setText(_translate("MainWindow", "Nuevo producto"))
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_0").clicked.connect(self.new_product)
        else:
            pass

        self.fme_lbl_title.setStyleSheet("#fme_lbl_title { background-image : url(:/icon/assets/icon/store2.png);}")
        self.lbl_title.setText(" CATEGORÍAS")

        self.__load_content_area()


    def new_product(self):
        self.__application.ui_config_modal("new_product")

    def new_category(self):
        self.__application.ui_config_modal("new_category")

    def __logout(self):
        self.__application.user = ""
        self.__application.is_superuser = False
        self.__application.is_staff = False
        self.__application.ui_config("login")

    def __clean(self, name="QTableWidget"):
        if name == "QTableWidget":
            data = self.frame_3.findChildren(QtWidgets.QPushButton)
            for qwidget in data:
                qwidget.deleteLater()

    def __load(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT id, name FROM bhhj3cug6bdknptqdl7k.category_db"
            self.category_data = self._connector.run_query(sql)
            if self.category_data:
                pass
        else:
            pass

    def __add_card(self):
        pass

    def __remove_cards(self):
        pass

    def __load_content_area(self):
        self.__load()
        frame = QtWidgets.QFrame(self.centralwidget)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setMidLineWidth(0)
        frame.setObjectName("frame_0")
        horizontal_layout_0 = QtWidgets.QHBoxLayout(frame)
        horizontal_layout_0.setContentsMargins(11, -1, -1, -1)
        horizontal_layout_0.setObjectName("horizontal_layout_0")
        for category in self.category_data:
            card = CardController(category=category)
            card.setObjectName(str(category[1]))
            horizontal_layout_0.addWidget(card)

        self.scrollAreaWidgetContents.addWidget(frame)

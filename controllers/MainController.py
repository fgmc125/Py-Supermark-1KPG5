from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QSpacerItem, QLayoutItem
from PyQt5.uic import loadUi

from controllers.CategoryCardController import CategoryCardController
from controllers.ProductCardController import ProductCardController
from controllers.ProductController import ProductController
from controllers.UserCardController import UserCardController
from mysqlhelper.Conector import Conexion
from views.assets import *


class MainController(QMainWindow):
    def __init__(self, __application):
        super(MainController, self).__init__()
        self._application = __application
        loadUi('views/MainView.ui', self)
        self.__isToggler = True
        self._connector = None
        self.category_data = None
        self.category_cards = None
        self.q_spacer_item = None

        self.__setupUiComponents()

    def __setupUiComponents(self):
        if self._application.is_staff:
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

        self.btn_username.setText(self._application.user)

        self.lbl_version.setText(self._application.getTitle())
        self.btn_toggler.clicked.connect(self.__toggler_action)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_0").clicked.connect(self.__show_home)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_1").clicked.connect(self.__action_button_1)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_2").clicked.connect(self.__show_categories)
        self.fme_aside.findChild(QtWidgets.QPushButton, "btn_exit").clicked.connect(self.__logout)

    def __toggler_action(self):
        if self.__isToggler:
            self.fme_aside.setMaximumWidth(160)
            self.fme_aside.setMinimumWidth(160)
            self.btn_toggler.setText(" MENÚ")
            self.btn_0.setText(" INICIO")
            self.btn_1.setText("  USUARIOS")
            self.btn_2.setText(" CATEGORÍAS")
            self.btn_exit.setText(" CERRAR SESIÓN")
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
        self.__clean()
        self.__clean(name="Cards")

        _translate = QtCore.QCoreApplication.translate
        if self._application.is_staff:
            self.btn_item_var_0 = QtWidgets.QPushButton(self.frame_3)
            self.btn_item_var_0.setObjectName("btn_item_var_0")
            self.horizontalLayout_10.addWidget(self.btn_item_var_0)
            self.btn_item_var_0.setText(_translate("MainWindow", "Nuevo usuario"))
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_0").clicked.connect(self.new_user)

            self._load_content_area_with_users()
        else:
            self.btn_item_var_0 = QtWidgets.QPushButton(self.frame_3)
            self.btn_item_var_0.setObjectName("btn_item_var_0")
            self.horizontalLayout_10.addWidget(self.btn_item_var_0)
            self.btn_item_var_0.setText(_translate("MainWindow", "Carrito"))
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_0").clicked.connect(self.new_user)

            self.btn_item_var_1 = QtWidgets.QPushButton(self.frame_3)
            self.btn_item_var_1.setObjectName("btn_item_var_1")
            self.horizontalLayout_10.addWidget(self.btn_item_var_1)
            self.btn_item_var_1.setText(_translate("MainWindow", "Guardados"))
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_0").clicked.connect(self.new_user)

        self.fme_lbl_title.setStyleSheet(self.btn_1_stylesheet)
        self.lbl_title.setText(self.btn_1_title)

    def __show_home(self):
        self.__clean()
        self.__clean(name="Cards")
        self.fme_lbl_title.setStyleSheet("#fme_lbl_title { background-image : url(:/icon/assets/icon/house2.png);}")
        self.lbl_title.setText(" INICIO")

    def __show_categories(self):
        _translate = QtCore.QCoreApplication.translate
        if self._application.is_staff:
            self.__clean()
            self.__clean(name="Cards")
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

            self.btn_item_var_2 = QtWidgets.QPushButton(self.frame_3)
            self.btn_item_var_2.setObjectName("btn_item_var_2")
            self.horizontalLayout_10.addWidget(self.btn_item_var_2)
            self.btn_item_var_2.setText(_translate("MainWindow", "Recargar DB"))
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_2").clicked.connect(self.refresh)
        else:
            pass

        self.fme_lbl_title.setStyleSheet("#fme_lbl_title { background-image : url(:/icon/assets/icon/store2.png);}")
        self.lbl_title.setText(" CATEGORÍAS")

        self._load_content_area()

    def new_user(self):
        self._application.ui_config_modal("new_user")

    def new_product(self):
        self._application.ui_config_modal("new_product")

    def new_category(self):
        self._application.ui_config_modal("new_category")

    def __logout(self):
        self._application.user = ""
        self._application.is_superuser = False
        self._application.is_staff = False
        self._application.ui_config("login")

    def __clean(self, name="QTableWidget"):
        if name == "QTableWidget":
            data = self.frame_3.findChildren(QtWidgets.QPushButton)
            for qwidget in data:
                qwidget.deleteLater()
        elif name == "Cards":
            if self.q_spacer_item:
                self.verticalLayout_13.removeItem(self.q_spacer_item)
            data = self.scrollAreaWidgetContents.findChildren(CategoryCardController)
            for qwidget in data:
                qwidget.deleteLater()
            data = self.scrollAreaWidgetContents.findChildren(QtWidgets.QFrame)
            for qwidget in data:
                qwidget.deleteLater()

    def __load(self):
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT id, name FROM bhhj3cug6bdknptqdl7k.category_db"
            self.category_data = self._connector.run_query(sql)
            self._connector.close()

    def _load_content_area(self):
        self.__clean(name="Cards")

        cnt_cards_for_row = int((self.geometry().width() - 86) / 239)
        categories_split = [self._application.categories_data[i:i + cnt_cards_for_row] for i in
                            range(0, len(self._application.categories_data), cnt_cards_for_row)]
        cnt = 1  # solo para debug
        for x in range(len(categories_split)):
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame_" + str(x))

            horizontal_layout = QtWidgets.QHBoxLayout(frame)
            horizontal_layout.setContentsMargins(0, 0, 0, 0)
            horizontal_layout.setObjectName("horizontal_layout_" + str(x))

            for category in categories_split[x]:
                card = CategoryCardController(category=category,
                                              main_controller=self,
                                              product_data=self._application.products_data[category[1]]
                                              )
                card.setObjectName(str(category[1]))
                horizontal_layout.addWidget(card)

                print("DEBUG: %", int(cnt * 100 / len(self._application.categories_data)))  # solo para debug
                cnt += 1  # solo para debug

            horizontal_layout.addItem(
                QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
            self.verticalLayout_13.addWidget(frame)

        self.q_spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(self.q_spacer_item)

    def _reformat_content(self, category_name, __product_data):
        self.__clean(name="Cards")
        self.lbl_title.setText(" CATEGORÍAS / " + str(category_name).upper())

        cnt_cards_for_row = int((self.geometry().width() - 86) / 239)
        products_split = [__product_data[i:i + cnt_cards_for_row] for i in
                          range(0, len(list(__product_data)), cnt_cards_for_row)]
        cnt = 1

        for x in range(len(products_split)):
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame_" + str(x))

            horizontal_layout = QtWidgets.QHBoxLayout(frame)
            horizontal_layout.setContentsMargins(0, 0, 0, 0)
            horizontal_layout.setObjectName("horizontal_layout_" + str(x))

            for product in products_split[x]:
                card = ProductCardController(product=product, main_controller=self)
                card.setObjectName(str(product[1]))
                horizontal_layout.addWidget(card)

                print("DEBUG: %", int(cnt * 100 / len(__product_data)))
                cnt += 1

            horizontal_layout.addItem(
                QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
            self.verticalLayout_13.addWidget(frame)

        self.q_spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(self.q_spacer_item)

    def _load_content_area_with_users(self):
        self.__clean(name="Cards")

        users = None
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = """SELECT id,username,first_name,last_name,date_joined,last_login,is_superuser,is_staff FROM bhhj3cug6bdknptqdl7k.user_db"""
            users = self._connector.run_query(sql)
            self._connector.close()


        cnt_cards_for_row = int((self.geometry().width() - 86) / 239)
        users_split = [users[i:i + cnt_cards_for_row] for i in range(0, len(users), cnt_cards_for_row)]
        cnt = 1  # solo para debug
        for x in range(len(users_split)):
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame_" + str(x))

            horizontal_layout = QtWidgets.QHBoxLayout(frame)
            horizontal_layout.setContentsMargins(0, 0, 0, 0)
            horizontal_layout.setObjectName("horizontal_layout_" + str(x))

            for user in users_split[x]:
                card = UserCardController(user=user, main_controller=self)
                card.setObjectName(str(user[1]))
                horizontal_layout.addWidget(card)

                print("DEBUG: %", int(cnt * 100 / len(users)))  # solo para debug
                cnt += 1  # solo para debug

            horizontal_layout.addItem(
                QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
            self.verticalLayout_13.addWidget(frame)

        self.q_spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(self.q_spacer_item)

    def _load_product_view(self, product_data, category):
        self.__clean(name="Cards")
        self.lbl_title.setText(self.lbl_title.text() + " / " + str(product_data[1]).upper())

        frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame_00")

        horizontal_layout = QtWidgets.QHBoxLayout(frame)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setObjectName("horizontal_layout_00")

        card = ProductController(main_controller=self, product=product_data, category=category)
        card.setObjectName(str(product_data[1]))
        horizontal_layout.addWidget(card)

        self.verticalLayout_13.addWidget(frame)
        self.verticalLayout_13.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

    def ui_config_modal(self, ui_modal, id=None):
        self._application.ui_config_modal(ui_modal, id)

    def refresh(self):
        self._application.load_data()
        self._load_content_area()


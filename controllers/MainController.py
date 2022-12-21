from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QSpacerItem, QLayoutItem, QTableWidgetItem
from PyQt5.uic import loadUi

from controllers.CartCardController import CartCardController
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
        self.fme_lbl_title.setStyleSheet("#fme_lbl_title { background-image : url(:/icon/assets/icon/house2.png);}")

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

        self.btn_show_in_table.clicked.connect(self.__show_in_table)
        #self.show_with_cards.clicked.connect(self.__show_with_cards)
        self.btn_search.clicked.connect(self.__search_products)

    def __search_products(self):
        product_data = None
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT * FROM bhhj3cug6bdknptqdl7k.product_db where name regexp '" + self.tfd_input.text() + "'"
            product_data = self._connector.run_query(sql)
            self._connector.close()

        self._load_content_area_with_products("RESULTADOS: "+str(len(product_data)), list(product_data))

    def __toggler_action(self):
        if self.__isToggler:
            self.fme_aside.setMaximumWidth(160)
            self.fme_aside.setMinimumWidth(160)
            self.btn_toggler.setText(" MENÚ")
            self.btn_0.setText(" INICIO")
            if self._application.is_staff:
                self.btn_1.setText("  USUARIOS")
            else:
                self.btn_1.setText("  MI CARRITO")
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
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_0").clicked.connect(self.__show_my_cart)

            self.btn_item_var_1 = QtWidgets.QPushButton(self.frame_3)
            self.btn_item_var_1.setObjectName("btn_item_var_1")
            self.horizontalLayout_10.addWidget(self.btn_item_var_1)
            self.btn_item_var_1.setText(_translate("MainWindow", "Guardados"))
            self.frame_3.findChild(QtWidgets.QPushButton, "btn_item_var_1").clicked.connect(self.__show_saved)

            self._load_content_area_with_carts()

        self.fme_lbl_title.setStyleSheet(self.btn_1_stylesheet)
        self.lbl_title.setText(self.btn_1_title)

    def __show_saved(self):
        self.lbl_title.setText(" GUARDADOS")
        self._load_content_area_with_carts(show_saved=True, needs_update=False)

    def __show_my_cart(self):
        self.lbl_title.setText(" MI CARRITO")
        self._load_content_area_with_carts(needs_update=False)

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

        self._load_content_area_with_categories()

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

    def _load_content_area_with_categories(self, needs_update=True, show_in_table=False):
        self.__clean(name="Cards")

        cnt_cards_for_row = int((self.geometry().width() - 86) / 239)
        categories_split = [self._application.categories_data[i:i + cnt_cards_for_row] for i in
                            range(0, len(self._application.categories_data), cnt_cards_for_row)]

        if show_in_table:
            #self.__clean()
            self.__qtable(header=["ID", "NOMBRE", "IMAGEN", "DESCRIPCION"],
                          data=self._application.categories_data)
        else:
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

            self.q_spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                       QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_13.addItem(self.q_spacer_item)

    def _load_content_area_with_products(self, category_name, __product_data, needs_update=True, show_in_table=False):
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

    def _load_content_area_with_users(self, needs_update=True, show_in_table=False):
        self.__clean(name="Cards")

        users = None
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = """SELECT id,username,first_name,last_name,email,date_joined,last_login,is_superuser,is_staff FROM bhhj3cug6bdknptqdl7k.user_db"""
            users = self._connector.run_query(sql)
            self._connector.close()

        if show_in_table:
            #self.__clean()
            self.__qtable(header=["ID", "USUARIO", "NOMBRE", "APELLIDO", "EMAIL", "CREADO", "ACTUALIZACIÓN", "SUPER USUARIO", "STAFF"],
                          data=users)
        else:
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

            self.q_spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                       QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_13.addItem(self.q_spacer_item)


    def _load_content_area_with_carts(self, show_saved=False, needs_update=True, show_in_table=False):
        self.__clean(name="Cards")

        if needs_update:
            self._connector = Conexion()
            if self._connector.is_connected():
                sql = """SELECT id,amount,saved,product_id,user_id FROM bhhj3cug6bdknptqdl7k.shopping_cart_db"""
                self._application.shopping_cart = self._connector.run_query(sql)
                self._connector.close()

        items_cart = list()
        cnt_cards_for_row = int((self.geometry().width() - 90) / 240)

        if show_saved:
            for item in self._application.shopping_cart:
                if item[2] == 1:
                    items_cart.append(item)
        else:
            for item in self._application.shopping_cart:
                if item[2] == 0:
                    items_cart.append(item)

        shopping_cart_split = [items_cart[i:i + cnt_cards_for_row] for i in
                               range(0, len(items_cart), cnt_cards_for_row)]

        if show_in_table:
            #self.__clean()
            self.__qtable(header=["ID", "CANTIDAD", "GUARDADO", "PRODUCTO", "USUARIO"],
                          data=items_cart)
        else:
            cnt = 1  # solo para debug
            for x in range(len(shopping_cart_split)):
                frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
                frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame.setFrameShadow(QtWidgets.QFrame.Raised)
                frame.setObjectName("frame_" + str(x))

                horizontal_layout = QtWidgets.QHBoxLayout(frame)
                horizontal_layout.setContentsMargins(0, 0, 0, 0)
                horizontal_layout.setObjectName("horizontal_layout_" + str(x))

                for item in shopping_cart_split[x]:
                    card = CartCardController(user=self._application.user_id, item=item, main_controller=self)
                    card.setObjectName(str(item[1]))
                    horizontal_layout.addWidget(card)

                    print("DEBUG: %", int(cnt * 100 / len(items_cart)))  # solo para debug
                    cnt += 1  # solo para debug

                horizontal_layout.addItem(
                    QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
                self.verticalLayout_13.addWidget(frame)

            self.q_spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                       QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_13.addItem(self.q_spacer_item)

    def __show_in_table(self):
        if "CATEGORÍAS" in self.lbl_title.text():
            self._load_content_area_with_categories(needs_update=False, show_in_table=True)

        elif "CATEGORÍAS / " in self.lbl_title.text():
            category_temp = self.lbl_title.text()[self.lbl_title.text().find('/')+1:].title()
            for item in self._application.categories_data:
                if item[1] == category_temp:
                    category_temp = item
                    break
            self._load_content_area_with_products(category_temp, self._application.products_data[category_temp], show_in_table=True)

            pass
        elif "CATEGORÍAS" in self.lbl_title.text() and self.lbl_title.text().count('/') == 2:
            index_temp = self.lbl_title.text().rfind('/')
            category_temp = self.lbl_title.text()[self.lbl_title.text().find('/')+1:index_temp-1].title()
            product_temp = self.lbl_title.text()[index_temp+1:].title()
            for item in self._application.products_data[category_temp]:
                if item[1] == product_temp:
                    product_temp = item
                    break
            for item in self._application.categories_data:
                if item[1] == category_temp:
                    category_temp = item
                    break
            self._load_product_view(product_temp, category_temp, show_in_table=True)
        elif "MI CARRITO" in self.lbl_title.text():
            self._load_content_area_with_carts(show_saved=False, needs_update=False, show_in_table=True)
        elif "USUARIOS" in self.lbl_title.text():
            self._load_content_area_with_users(needs_update=True, show_in_table=True)

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
        self._load_content_area_with_categories()

    def __qtable(self, header, data):
        _translate = QtCore.QCoreApplication.translate

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setStyleSheet("""QTableView {
    background-color: transparent;
    font-size:13px;
}

QHeaderView::section:horizontal {
    color: #fff;
    border-style: solid;
    background-color: #1877F2;
 }

QTableWidget {
    border: 2px solid #1877F2;
    border-top-color: #1877F2;
    gridline-color: #616161;
    selection-background-color: #616161;
    color:#333;
    font-size:12px;
 }""")
        self.tableWidget.setGeometry(QtCore.QRect(130, 150, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_13.addWidget(self.tableWidget)

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
        self.tableWidget.verticalHeader().setVisible(True)
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


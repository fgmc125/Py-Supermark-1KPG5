# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/MainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/* ----------------------------- Body ----------------------------- */\n"
"\n"
"QMainWindows, QFrame {\n"
"    margin : 0px;\n"
"    padding : 0px;\n"
"}\n"
"\n"
"QMainWindows {\n"
"    background-color : #FFF;\n"
"}\n"
"\n"
"/* --------------------------- Header ---------------------------- */\n"
"\n"
"#fme_header {\n"
"    background-color : #FFF;\n"
"    min-height : 70px;\n"
"    max-height : 70px;\n"
"}\n"
"\n"
"#fme_primary_nav {\n"
"    min-height : 70px;\n"
"    max-height : 70px;\n"
"}\n"
"\n"
"#fme_secondary_nav {\n"
"    min-height : 40px;\n"
"    max-height : 40px;\n"
"}\n"
"\n"
"/* ----------------------------- Logo ----------------------------- */\n"
"\n"
"#fme_logo {\n"
"    min-width : 38px;\n"
"    max-width : 38px;\n"
"    min-height : 38px;\n"
"    max-height : 38px;\n"
"}\n"
"\n"
"#lbl_version, #lbl_my_cart, #lbl_username {\n"
"    color: #20ACD4;\n"
"}\n"
"\n"
"#lbl_brand, #lbl_cnt_cart, #lbl_type {\n"
"    color: #5E6065;\n"
"}\n"
"\n"
"/* ----------------------- Aside Menu --------------------------- */\n"
"\n"
"#fme_aside {\n"
"    background-color : #1877F2; /*#265792*/\n"
"    min-width : 51px;\n"
"    max-width : 51px;\n"
"}\n"
"\n"
"/* ------------------------- Content ----------------------------- */\n"
"\n"
"#fme_content {\n"
"    background-color : #F0F3F6;\n"
"}\n"
"\n"
"#fme_footer {\n"
"    background-color : #E5E6E7;\n"
"    max-height: 20px;\n"
"}\n"
"\n"
"/* ------------------------- ToolTip ------------------------------ */\n"
"\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: #5E6065;\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 3px solid #31AFD6;\n"
"    text-align: left;\n"
"    padding: 8px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fme_aside = QtWidgets.QFrame(self.centralwidget)
        self.fme_aside.setStyleSheet("#fme_toggler:hover, #fme_config:hover, #fme_btn_0:hover, #fme_btn_1:hover, #fme_btn_2:hover {\n"
"    background-color : #5E6065;/*42B72A;*/\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding-left : 11px;\n"
"    padding-right : 11px;\n"
"    border: None;\n"
"    qproperty-iconSize: 25px;\n"
"    text-align: left;\n"
"    color : #FFF;\n"
"}\n"
"\n"
"#btn_exit{\n"
"    padding-top : 12px;\n"
"    padding-bottom : 12px;\n"
"    qproperty-icon: url(:/icon/assets/icon/exit.png);\n"
"    qproperty-text: \"\";\n"
"}\n"
"\n"
"#btn_toggler {\n"
"    padding-top : 12px;\n"
"    padding-bottom : 12px;\n"
"    qproperty-icon: url(:/icon/assets/icon/bars.png);\n"
"    qproperty-text: \"\";\n"
"}\n"
"\n"
"#btn_0 {\n"
"    padding-top : 6px;\n"
"    padding-bottom : 6px;\n"
"    qproperty-icon: url(:/icon/assets/icon/house.png);\n"
"    qproperty-text: \"\";\n"
"}\n"
"\n"
"#btn_1 {\n"
"    padding-top : 6px;\n"
"    padding-bottom : 6px;\n"
"    \n"
"    qproperty-text: \"\";\n"
"}\n"
"\n"
"#btn_2 {\n"
"    padding-top : 6px;\n"
"    padding-bottom : 6px;\n"
"    qproperty-icon: url(:/icon/assets/icon/store.png);\n"
"    qproperty-text: \"\";\n"
"}")
        self.fme_aside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_aside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_aside.setMidLineWidth(0)
        self.fme_aside.setObjectName("fme_aside")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fme_aside)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fme_toggler = QtWidgets.QFrame(self.fme_aside)
        self.fme_toggler.setMinimumSize(QtCore.QSize(0, 0))
        self.fme_toggler.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_toggler.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_toggler.setObjectName("fme_toggler")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.fme_toggler)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btn_toggler = QtWidgets.QPushButton(self.fme_toggler)
        self.btn_toggler.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_toggler.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_toggler.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_toggler.setText("")
        self.btn_toggler.setObjectName("btn_toggler")
        self.verticalLayout_11.addWidget(self.btn_toggler)
        self.verticalLayout.addWidget(self.fme_toggler)
        spacerItem = QtWidgets.QSpacerItem(20, 189, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.fme_left_nav = QtWidgets.QFrame(self.fme_aside)
        self.fme_left_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_left_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_left_nav.setObjectName("fme_left_nav")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fme_left_nav)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fme_btn_1 = QtWidgets.QFrame(self.fme_left_nav)
        self.fme_btn_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_btn_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_btn_1.setObjectName("fme_btn_1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fme_btn_1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btn_1 = QtWidgets.QPushButton(self.fme_btn_1)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setToolTipDuration(-1)
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.verticalLayout_9.addWidget(self.btn_1)
        self.verticalLayout_3.addWidget(self.fme_btn_1)
        self.fme_btn_0 = QtWidgets.QFrame(self.fme_left_nav)
        self.fme_btn_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_btn_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_btn_0.setObjectName("fme_btn_0")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fme_btn_0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn_0 = QtWidgets.QPushButton(self.fme_btn_0)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_0.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_0.setText("")
        self.btn_0.setObjectName("btn_0")
        self.verticalLayout_10.addWidget(self.btn_0)
        self.verticalLayout_3.addWidget(self.fme_btn_0)
        self.fme_btn_2 = QtWidgets.QFrame(self.fme_left_nav)
        self.fme_btn_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_btn_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_btn_2.setObjectName("fme_btn_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.fme_btn_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_2 = QtWidgets.QPushButton(self.fme_btn_2)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.verticalLayout_8.addWidget(self.btn_2)
        self.verticalLayout_3.addWidget(self.fme_btn_2)
        self.verticalLayout.addWidget(self.fme_left_nav)
        spacerItem1 = QtWidgets.QSpacerItem(20, 190, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.fme_config = QtWidgets.QFrame(self.fme_aside)
        self.fme_config.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_config.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_config.setObjectName("fme_config")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fme_config)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_exit = QtWidgets.QPushButton(self.fme_config)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setText("")
        self.btn_exit.setIconSize(QtCore.QSize(25, 25))
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_4.addWidget(self.btn_exit)
        self.verticalLayout.addWidget(self.fme_config)
        self.horizontalLayout.addWidget(self.fme_aside)
        self.fme_body = QtWidgets.QFrame(self.centralwidget)
        self.fme_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_body.setObjectName("fme_body")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fme_body)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fme_header = QtWidgets.QFrame(self.fme_body)
        self.fme_header.setStyleSheet("#tfd_input {\n"
"    background-color: #F0F3F6;\n"
"    color: #5E6065;\n"
"    border : 1px solid;\n"
"    border-color: #F0F3F6;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"}\n"
"\n"
"#btn_search {\n"
"    background-color: #1877F2;\n"
"    border : 1px solid;\n"
"    border-color: #1877F2;\n"
"    border-bottom-right-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"\n"
"#lbl_version {\n"
"    color: #20ACD4;\n"
"}")
        self.fme_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_header.setObjectName("fme_header")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fme_header)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fme_primary_nav = QtWidgets.QFrame(self.fme_header)
        self.fme_primary_nav.setStyleSheet("")
        self.fme_primary_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_primary_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_primary_nav.setObjectName("fme_primary_nav")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fme_primary_nav)
        self.horizontalLayout_7.setContentsMargins(11, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.fme_logograma = QtWidgets.QFrame(self.fme_primary_nav)
        self.fme_logograma.setMinimumSize(QtCore.QSize(0, 0))
        self.fme_logograma.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fme_logograma.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_logograma.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_logograma.setObjectName("fme_logograma")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fme_logograma)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fme_logo = QtWidgets.QFrame(self.fme_logograma)
        self.fme_logo.setMinimumSize(QtCore.QSize(40, 40))
        self.fme_logo.setMaximumSize(QtCore.QSize(40, 40))
        self.fme_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_logo.setObjectName("fme_logo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fme_logo)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.fme_logo)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/assets/img/logo_python.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.fme_logo)
        self.frame_2 = QtWidgets.QFrame(self.fme_logograma)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbl_brand = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_brand.setFont(font)
        self.lbl_brand.setObjectName("lbl_brand")
        self.verticalLayout_7.addWidget(self.lbl_brand)
        self.lbl_version = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbl_version.setFont(font)
        self.lbl_version.setObjectName("lbl_version")
        self.verticalLayout_7.addWidget(self.lbl_version)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_7.addWidget(self.fme_logograma)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.btn_username = QtWidgets.QPushButton(self.fme_primary_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_username.sizePolicy().hasHeightForWidth())
        self.btn_username.setSizePolicy(sizePolicy)
        self.btn_username.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_username.setMaximumSize(QtCore.QSize(16777215, 32))
        self.btn_username.setStyleSheet("QPushButton {\n"
"    color : #6BA6FD;\n"
"    border-style : solid;\n"
"    border-radius: 5px;\n"
"    min-height : 32px;\n"
"    font : 77 18px \"Arial\";\n"
"    background-color : #DBE9FF;\n"
"    padding-left : 13px;\n"
"    padding-right : 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color : transparent;\n"
"    color : #6BA6FD;\n"
"    border: 1px solid #6BA6FD;\n"
"    border-radius: 5px;\n"
"}")
        self.btn_username.setObjectName("btn_username")
        self.horizontalLayout_7.addWidget(self.btn_username)
        self.fme_search = QtWidgets.QFrame(self.fme_primary_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fme_search.sizePolicy().hasHeightForWidth())
        self.fme_search.setSizePolicy(sizePolicy)
        self.fme_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_search.setObjectName("fme_search")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fme_search)
        self.horizontalLayout_5.setContentsMargins(10, 2, 10, 2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fme_search_input = QtWidgets.QFrame(self.fme_search)
        self.fme_search_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_search_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_search_input.setObjectName("fme_search_input")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fme_search_input)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tfd_input = QtWidgets.QLineEdit(self.fme_search_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tfd_input.sizePolicy().hasHeightForWidth())
        self.tfd_input.setSizePolicy(sizePolicy)
        self.tfd_input.setMinimumSize(QtCore.QSize(400, 32))
        self.tfd_input.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tfd_input.setFont(font)
        self.tfd_input.setToolTipDuration(-1)
        self.tfd_input.setAutoFillBackground(False)
        self.tfd_input.setCursorPosition(0)
        self.tfd_input.setObjectName("tfd_input")
        self.verticalLayout_6.addWidget(self.tfd_input)
        self.horizontalLayout_5.addWidget(self.fme_search_input)
        self.fme_search_button = QtWidgets.QFrame(self.fme_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fme_search_button.sizePolicy().hasHeightForWidth())
        self.fme_search_button.setSizePolicy(sizePolicy)
        self.fme_search_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_search_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_search_button.setObjectName("fme_search_button")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.fme_search_button)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_search = QtWidgets.QPushButton(self.fme_search_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_search.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_search.setFont(font)
        self.btn_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/assets/icon/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_6.addWidget(self.btn_search)
        self.horizontalLayout_5.addWidget(self.fme_search_button)
        self.horizontalLayout_7.addWidget(self.fme_search)
        self.verticalLayout_2.addWidget(self.fme_primary_nav)
        self.verticalLayout_5.addWidget(self.fme_header)
        self.fme_content = QtWidgets.QFrame(self.fme_body)
        self.fme_content.setToolTip("")
        self.fme_content.setStyleSheet("#fme_offers, #fme_title, #fme_card {\n"
"    background-color: #FFF;\n"
"    border : 1px solid;\n"
"    border-color: #FFF;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#fme_offers {\n"
"    min-height : 150px;\n"
"    max-height : 150px;\n"
"}\n"
"\n"
"#fme_title {\n"
"    min-height : 70px;\n"
"    max-height : 70px;\n"
"}\n"
"\n"
"#fme_lbl_title {\n"
"    min-width : 42px;\n"
"    max-width : 42px;\n"
"    background-image : url(:/icon/assets/icon/store2.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#lbl_title {\n"
"    font : 18px \"Arial\";\n"
"    color: #5E6065;\n"
"    qproperty-text: \"INICIO\";\n"
"}")
        self.fme_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_content.setObjectName("fme_content")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.fme_content)
        self.verticalLayout_12.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        # inicio
        self.fme_title = QtWidgets.QFrame(self.fme_content)
        self.fme_title.setStyleSheet("QPushButton {\n"
"    color : #FFF;\n"
"    border-style : solid;\n"
"    border-radius: 5px;\n"
"    min-height : 40px;\n"
"    font : 77 18px \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #FFF;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#btn_item_var_0:pressed, #btn_item_var_1:pressed {\n"
"    background-color : transparent;\n"
"    color : #42B72A;\n"
"    border: 1px solid #42B72A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#btn_item_var_0, #btn_item_var_1 {\n"
"    background-color : #42B72A;\n"
"    padding-left : 10px;\n"
"    padding-right : 10px;\n"
"}\n"
"")
        self.fme_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_title.setObjectName("fme_title")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.fme_title)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(self.fme_title)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fme_lbl_title = QtWidgets.QFrame(self.frame)
        self.fme_lbl_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_lbl_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_lbl_title.setObjectName("fme_lbl_title")
        self.horizontalLayout_2.addWidget(self.fme_lbl_title)
        self.lbl_title = QtWidgets.QLabel(self.frame)
        self.lbl_title.setWordWrap(False)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayout_2.addWidget(self.lbl_title)
        self.horizontalLayout_8.addWidget(self.frame)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)

        self.frame_3 = QtWidgets.QFrame(self.fme_title)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.btn_item_var_1 = QtWidgets.QPushButton(self.frame_3)
        self.btn_item_var_1.setObjectName("btn_item_var_1")
        self.horizontalLayout_10.addWidget(self.btn_item_var_1)

        self.btn_item_var_0 = QtWidgets.QPushButton(self.frame_3)
        self.btn_item_var_0.setObjectName("btn_item_var_0")
        self.horizontalLayout_10.addWidget(self.btn_item_var_0)

        self.horizontalLayout_8.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.fme_title)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/assets/icon/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_12.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/assets/icon/table-cells-large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_12.addWidget(self.pushButton)
        self.horizontalLayout_8.addWidget(self.frame_4)
        self.verticalLayout_12.addWidget(self.fme_title)
        self.fme_cards = QtWidgets.QFrame(self.fme_content)
        self.fme_cards.setStyleSheet("QFrame {\n"
"    background-color: #FFF;\n"
"    border : 1px solid;\n"
"    border-color: transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#fme_cards {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#fme_icon_card_0, #fme_icon_card_1, #fme_icon_card_2 {\n"
"    background-position: center center;\n"
"    background-repeat: no-repeat;\n"
"    min-height : 130px;\n"
"    max-height : 130px;\n"
"}\n"
"\n"
"#fme_icon_card_0 {\n"
"    background-image : url(:/images/assets/img/cart-shopping.png);\n"
"}\n"
"\n"
"#fme_icon_card_1 {\n"
"    background-image : url(:/images/assets/img/basket.png);\n"
"}\n"
"\n"
"#fme_icon_card_2 {\n"
"    background-image : url(:/images/assets/img/heart.png);\n"
"}\n"
"\n"
"#lbl_card_title_0, #lbl_card_title_1, #lbl_card_title_2 {\n"
"    color : #848688;\n"
"    font : 22px \"Arial\";\n"
"}\n"
"\n"
"#lbl_card_cnt_0, #lbl_card_cnt_1, #lbl_card_cnt_2 {\n"
"    color : #848688;\n"
"    font : 50px \"Arial\";\n"
"}")
        self.fme_cards.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_cards.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_cards.setObjectName("fme_cards")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.fme_cards)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fme_card_2 = QtWidgets.QFrame(self.fme_cards)
        self.fme_card_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_card_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_card_2.setObjectName("fme_card_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.fme_card_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_9.addWidget(self.fme_card_2)
        self.verticalLayout_12.addWidget(self.fme_cards)
        self.verticalLayout_5.addWidget(self.fme_content)
        self.fme_footer = QtWidgets.QFrame(self.fme_body)
        self.fme_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fme_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fme_footer.setObjectName("fme_footer")
        self.verticalLayout_5.addWidget(self.fme_footer)
        self.horizontalLayout.addWidget(self.fme_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_toggler.setToolTip(_translate("MainWindow", "Menú"))
        self.btn_1.setToolTip(_translate("MainWindow", "Perfil"))
        self.btn_0.setToolTip(_translate("MainWindow", "Inicio"))
        self.btn_2.setToolTip(_translate("MainWindow", "Artículos"))
        self.btn_exit.setToolTip(_translate("MainWindow", "Cerrar sesión"))
        self.lbl_brand.setText(_translate("MainWindow", "PySupermark"))
        self.lbl_version.setText(_translate("MainWindow", "v0.20221205"))
        self.btn_username.setText(_translate("MainWindow", "Username"))
        self.tfd_input.setPlaceholderText(_translate("MainWindow", " Buscar artículos"))
        self.lbl_title.setText(_translate("MainWindow", "INICIO"))
        self.btn_item_var_1.setText(_translate("MainWindow", "Nueva categoría"))
        self.btn_item_var_0.setText(_translate("MainWindow", "Nuevo producto"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

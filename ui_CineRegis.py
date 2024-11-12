# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CineRegis.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1122, 794)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239); \n"
"}\n"
"QPushButton{\n"
"  color:white;\n"
"  height:30px;\n"
"  border:none;\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"   background-color: #F5FAFE;\n"
"   color:#1F95EF; \n"
"   font-weight:bold;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/images/images/CineRegis.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.home_1 = QPushButton(self.icon_only_widget)
        self.home_1.setObjectName(u"home_1")
        icon = QIcon()
        icon.addFile(u":/icon/Icon/home_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icon/Icon/home_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.home_1.setIcon(icon)
        self.home_1.setIconSize(QSize(30, 30))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_1)

        self.search_1 = QPushButton(self.icon_only_widget)
        self.search_1.setObjectName(u"search_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Icon/search_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icon/Icon/search_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.search_1.setIcon(icon1)
        self.search_1.setIconSize(QSize(30, 30))
        self.search_1.setCheckable(True)
        self.search_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.search_1)

        self.movie_1 = QPushButton(self.icon_only_widget)
        self.movie_1.setObjectName(u"movie_1")
        icon2 = QIcon()
        icon2.addFile(u":/icon/Icon/movie_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icon/Icon/movie_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.movie_1.setIcon(icon2)
        self.movie_1.setIconSize(QSize(30, 30))
        self.movie_1.setCheckable(True)
        self.movie_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.movie_1)

        self.ticket_1 = QPushButton(self.icon_only_widget)
        self.ticket_1.setObjectName(u"ticket_1")
        icon3 = QIcon()
        icon3.addFile(u":/icon/Icon/book_online_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icon/Icon/book_online_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ticket_1.setIcon(icon3)
        self.ticket_1.setIconSize(QSize(30, 30))
        self.ticket_1.setCheckable(True)
        self.ticket_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ticket_1)

        self.statistic_1 = QPushButton(self.icon_only_widget)
        self.statistic_1.setObjectName(u"statistic_1")
        icon4 = QIcon()
        icon4.addFile(u":/icon/Icon/analytics_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icon/Icon/analytics_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.statistic_1.setIcon(icon4)
        self.statistic_1.setIconSize(QSize(30, 30))
        self.statistic_1.setCheckable(True)
        self.statistic_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.statistic_1)

        self.user_1 = QPushButton(self.icon_only_widget)
        self.user_1.setObjectName(u"user_1")
        icon5 = QIcon()
        icon5.addFile(u":/icon/Icon/person_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icon/Icon/person_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.user_1.setIcon(icon5)
        self.user_1.setIconSize(QSize(30, 30))
        self.user_1.setCheckable(True)
        self.user_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.user_1)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(28, 337, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon6 = QIcon()
        icon6.addFile(u":/icon/Icon/settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icon/Icon/settings_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon6)
        self.settings_1.setIconSize(QSize(30, 30))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_1)

        self.logout_1 = QPushButton(self.icon_only_widget)
        self.logout_1.setObjectName(u"logout_1")
        icon7 = QIcon()
        icon7.addFile(u":/icon/Icon/logout_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icon/Icon/logout_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.logout_1.setIcon(icon7)
        self.logout_1.setIconSize(QSize(30, 30))
        self.logout_1.setCheckable(True)
        self.logout_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.logout_1)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239); \n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"  color:white;\n"
"  text-align:left;\n"
"  height:30px;\n"
"  border:none;\n"
"  padding-left:10px;\n"
"  border-top-left-radius:10px;\n"
"  border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"   background-color: #F5FAFE;\n"
"   color:#1F95EF; \n"
"   font-weight:bold;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 9, 9, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/images/images/CineRegis.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.home_2 = QPushButton(self.icon_name_widget)
        self.home_2.setObjectName(u"home_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.home_2.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/icon/Icon/home_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_2.setIcon(icon8)
        self.home_2.setIconSize(QSize(30, 30))
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.home_2)

        self.search_2 = QPushButton(self.icon_name_widget)
        self.search_2.setObjectName(u"search_2")
        self.search_2.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/icon/Icon/search_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_2.setIcon(icon9)
        self.search_2.setIconSize(QSize(30, 30))
        self.search_2.setCheckable(True)
        self.search_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.search_2)

        self.movie_2 = QPushButton(self.icon_name_widget)
        self.movie_2.setObjectName(u"movie_2")
        self.movie_2.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/icon/Icon/movie_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movie_2.setIcon(icon10)
        self.movie_2.setIconSize(QSize(30, 30))
        self.movie_2.setCheckable(True)
        self.movie_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.movie_2)

        self.ticket_2 = QPushButton(self.icon_name_widget)
        self.ticket_2.setObjectName(u"ticket_2")
        self.ticket_2.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/icon/Icon/book_online_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ticket_2.setIcon(icon11)
        self.ticket_2.setIconSize(QSize(30, 30))
        self.ticket_2.setCheckable(True)
        self.ticket_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.ticket_2)

        self.statistic_2 = QPushButton(self.icon_name_widget)
        self.statistic_2.setObjectName(u"statistic_2")
        self.statistic_2.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/icon/Icon/analytics_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.statistic_2.setIcon(icon12)
        self.statistic_2.setIconSize(QSize(30, 30))
        self.statistic_2.setCheckable(True)
        self.statistic_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.statistic_2)

        self.user_2 = QPushButton(self.icon_name_widget)
        self.user_2.setObjectName(u"user_2")
        self.user_2.setFont(font1)
        icon13 = QIcon()
        icon13.addFile(u":/icon/Icon/person_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_2.setIcon(icon13)
        self.user_2.setIconSize(QSize(30, 30))
        self.user_2.setCheckable(True)
        self.user_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.user_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(28, 337, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        font2 = QFont()
        font2.setPointSize(8)
        self.settings_2.setFont(font2)
        icon14 = QIcon()
        icon14.addFile(u":/icon/Icon/settings_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_2.setIcon(icon14)
        self.settings_2.setIconSize(QSize(30, 30))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.settings_2)

        self.logout_2 = QPushButton(self.icon_name_widget)
        self.logout_2.setObjectName(u"logout_2")
        self.logout_2.setFont(font2)
        icon15 = QIcon()
        icon15.addFile(u":/icon/Icon/logout_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_2.setIcon(icon15)
        self.logout_2.setIconSize(QSize(30, 30))
        self.logout_2.setCheckable(True)
        self.logout_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.logout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_7 = QVBoxLayout(self.main_menu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_17 = QPushButton(self.header_widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"border:none;")
        icon16 = QIcon()
        icon16.addFile(u"Icon/menu_24dp_000000_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon16)
        self.pushButton_17.setIconSize(QSize(35, 35))
        self.pushButton_17.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton_17)

        self.horizontalSpacer = QSpacerItem(230, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_18 = QPushButton(self.header_widget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        icon17 = QIcon()
        icon17.addFile(u"Icon/search_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_18.setIcon(icon17)
        self.pushButton_18.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_18)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(230, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_19 = QPushButton(self.header_widget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"border:none;")
        icon18 = QIcon()
        icon18.addFile(u"Icon/account_circle_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_19.setIcon(icon18)
        self.pushButton_19.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.pushButton_19)


        self.verticalLayout_7.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_4 = QLabel(self.home_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 230, 431, 111))
        font3 = QFont()
        font3.setPointSize(50)
        self.label_4.setFont(font3)
        self.stackedWidget.addWidget(self.home_page)
        self.search_page = QWidget()
        self.search_page.setObjectName(u"search_page")
        self.label_5 = QLabel(self.search_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 230, 491, 111))
        self.label_5.setFont(font3)
        self.stackedWidget.addWidget(self.search_page)
        self.movie_page = QWidget()
        self.movie_page.setObjectName(u"movie_page")
        self.label_6 = QLabel(self.movie_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 240, 431, 111))
        self.label_6.setFont(font3)
        self.stackedWidget.addWidget(self.movie_page)
        self.ticket_page = QWidget()
        self.ticket_page.setObjectName(u"ticket_page")
        self.label_7 = QLabel(self.ticket_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 290, 431, 111))
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.ticket_page)
        self.statistic_page = QWidget()
        self.statistic_page.setObjectName(u"statistic_page")
        self.label_8 = QLabel(self.statistic_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 281, 31))
        self.label_8.setFont(font2)
        self.widget = QWidget(self.statistic_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 791, 71))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239); \n"
"}\n"
"QPushButton{\n"
"  color:white;\n"
"  height:30px;\n"
"  border:none;\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"   background-color: #F5FAFE;\n"
"   color:#1F95EF; \n"
"   font-weight:bold;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.pushButton.setFont(font4)
        icon19 = QIcon()
        icon19.addFile(u"Icon/pie_chart_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon19)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font4)
        icon20 = QIcon()
        icon20.addFile(u"Icon/timeline_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon20)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font4)
        icon21 = QIcon()
        icon21.addFile(u"Icon/bar_chart_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon21)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.stackedWidget_2 = QStackedWidget(self.statistic_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(10, 160, 781, 521))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.graphicsView = QChartView(self.page)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 791, 521))
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.stackedWidget.addWidget(self.statistic_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.label_9 = QLabel(self.profile_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 180, 431, 111))
        self.label_9.setFont(font3)
        self.stackedWidget.addWidget(self.profile_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.label_10 = QLabel(self.setting_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 200, 561, 111))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.setting_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_17.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_17.toggled.connect(self.icon_name_widget.setVisible)
        self.user_1.toggled.connect(self.user_2.setChecked)
        self.statistic_1.toggled.connect(self.statistic_2.setChecked)
        self.ticket_1.toggled.connect(self.ticket_2.setChecked)
        self.movie_1.toggled.connect(self.movie_2.setChecked)
        self.search_1.toggled.connect(self.search_2.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.search_2.toggled.connect(self.search_1.setChecked)
        self.movie_2.toggled.connect(self.movie_1.setChecked)
        self.ticket_2.toggled.connect(self.ticket_1.setChecked)
        self.statistic_2.toggled.connect(self.statistic_1.setChecked)
        self.user_2.toggled.connect(self.user_1.setChecked)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.logout_1.toggled.connect(self.logout_2.setChecked)
        self.logout_2.toggled.connect(self.logout_1.setChecked)
        self.logout_1.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_1.setText("")
        self.search_1.setText("")
        self.movie_1.setText("")
        self.ticket_1.setText("")
        self.statistic_1.setText("")
        self.user_1.setText("")
        self.settings_1.setText("")
        self.logout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CineRegis", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.search_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.movie_2.setText(QCoreApplication.translate("MainWindow", u"Movie", None))
        self.ticket_2.setText(QCoreApplication.translate("MainWindow", u"Buy a tickets", None))
        self.statistic_2.setText(QCoreApplication.translate("MainWindow", u"Statistic", None))
        self.user_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.logout_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.pushButton_19.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Search page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"movie page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ticket page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Movie ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Pie Chart", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Line Chart", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Profile page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Settings page", None))
    # retranslateUi


from ui_CineRegis import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CineRegis")
        self.icon_only_widget.setHidden(True)

        self.home_1.clicked.connect(self.switch_to_home_page)
        self.home_2.clicked.connect(self.switch_to_home_page)

        self.search_1.clicked.connect(self.switch_to_search_page)
        self.search_2.clicked.connect(self.switch_to_search_page)
        
        self.movie_1.clicked.connect(self.switch_to_movie_page)
        self.movie_2.clicked.connect(self.switch_to_movie_page)

        self.ticket_1.clicked.connect(self.switch_to_ticket_page)
        self.ticket_2.clicked.connect(self.switch_to_ticket_page)
        
        self.statistic_1.clicked.connect(self.switch_to_statistic_page)
        self.statistic_2.clicked.connect(self.switch_to_statistic_page)

        self.user_1.clicked.connect(self.switch_to_profile_page)
        self.user_2.clicked.connect(self.switch_to_profile_page)

        self.settings_1.clicked.connect(self.switch_to_setting_page)
        self.settings_2.clicked.connect(self.switch_to_setting_page)

    def switch_to_home_page(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_search_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_movie_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_ticket_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_statistic_page(self):
        self.stackedWidget.setCurrentIndex(4)
    
    def switch_to_profile_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_setting_page(self):
        self.stackedWidget.setCurrentIndex(6)
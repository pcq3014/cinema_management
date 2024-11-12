from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView
from PyQt6 import uic
import pandas as pd
import sys

class MovieListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the .ui file using PyQt6's uic module
        uic.loadUi("movie_list.ui", self)
        
        # Connect UI elements to functions
        self.btnAdd.clicked.connect(self.add_movie)
        self.btnSaveToExcel.clicked.connect(self.save_to_excel)
        self.btnLoadFromExcel.clicked.connect(self.load_from_excel)
        
        # Set column headers to stretch evenly across the width
        self.movieTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.movie_data = []
        
        # Load Excel data when the application starts
        self.load_from_excel_on_start("movies.xlsx")

    def load_from_excel_on_start(self, file_path):
        try:
            df = pd.read_excel(file_path)
            self.movie_data = df.to_dict("records")
            self.movieTableWidget.setRowCount(0)
            for movie_info in self.movie_data:
                self.update_movie_table(movie_info)
        except FileNotFoundError:
            print("Excel file not found. Please ensure 'movies.xlsx' exists.")
        
    def add_movie(self):
        movie_id = self.movieIDLineEdit.text()
        name = self.nameLineEdit.text()
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        
        categories = []
        for index in range(self.categoryListWidget.count()):
            item = self.categoryListWidget.item(index)
            if item.isSelected():
                categories.append(item.text())

        if movie_id and name and categories:
            movie_info = {
                "Movie ID": movie_id,
                "Name": name,
                "Date": date,
                "Category": ", ".join(categories)
            }
            self.movie_data.append(movie_info)
            self.update_movie_table(movie_info)
        
        self.clear_inputs()

    def update_movie_table(self, movie_info):
        row = self.movieTableWidget.rowCount()
        self.movieTableWidget.insertRow(row)
        self.movieTableWidget.setItem(row, 0, QTableWidgetItem(str(movie_info["Movie ID"])))
        self.movieTableWidget.setItem(row, 1, QTableWidgetItem(movie_info["Name"]))
        self.movieTableWidget.setItem(row, 2, QTableWidgetItem(str(movie_info["Date"])))
        self.movieTableWidget.setItem(row, 3, QTableWidgetItem(movie_info["Category"]))

    def clear_inputs(self):
        self.movieIDLineEdit.clear()
        self.nameLineEdit.clear()
        self.dateEdit.setDate(self.dateEdit.minimumDate())
        for i in range(self.categoryListWidget.count()):
            item = self.categoryListWidget.item(i)
            item.setSelected(False)

    def save_to_excel(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save to Excel", "", "movies.xlsx")
        if file_path:
            df = pd.DataFrame(self.movie_data)
            df.to_excel(file_path, index=False)

    def load_from_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Load from Excel", "", "movies.xlsx")
        if file_path:
            df = pd.read_excel(file_path)
            self.movie_data = df.to_dict("records")
            self.movieTableWidget.setRowCount(0)  

            for movie_info in self.movie_data:
                self.update_movie_table(movie_info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieListApp()
    window.show()
    sys.exit(app.exec())

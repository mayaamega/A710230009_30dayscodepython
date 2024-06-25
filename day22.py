import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox


class PassengerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Daftar Penumpang Pesawat')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.passenger_table = QTableWidget()
        self.passenger_table.setColumnCount(3)
        self.passenger_table.setHorizontalHeaderLabels(['Nama', 'Umur', 'Jenis Kelamin'])
        self.layout.addWidget(self.passenger_table)

        self.add_passenger_button = QPushButton('Tambah Penumpang')
        self.add_passenger_button.clicked.connect(self.add_passenger_dialog)
        self.layout.addWidget(self.add_passenger_button)

        self.setLayout(self.layout)

        self.passengers = []

    def add_passenger_dialog(self):
        dialog = AddPassengerDialog(self)
        if dialog.exec_():
            name = dialog.name_line_edit.text()
            age = dialog.age_line_edit.text()
            gender = dialog.gender_line_edit.text()
            self.add_passenger(name, age, gender)

    def add_passenger(self, name, age, gender):
        self.passengers.append((name, age, gender))
        row_position = self.passenger_table.rowCount()
        self.passenger_table.insertRow(row_position)
        self.passenger_table.setItem(row_position, 0, QTableWidgetItem(name))
        self.passenger_table.setItem(row_position, 1, QTableWidgetItem(age))
        self.passenger_table.setItem(row_position, 2, QTableWidgetItem(gender))


class AddPassengerDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Tambah Penumpang')
        self.setText('Masukkan data penumpang:')
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        self.name_label = QLabel('Nama:')
        self.name_line_edit = QLineEdit()
        self.age_label = QLabel('Umur:')
        self.age_line_edit = QLineEdit()
        self.gender_label = QLabel('Jenis Kelamin:')
        self.gender_line_edit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_line_edit)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_line_edit)
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_line_edit)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PassengerWindow()
    window.show()
    sys.exit(app.exec_())
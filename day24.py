import sys
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jam")  
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)  # update every 1 second

        self.show_time()

    def show_time(self):
        current_time = QTime.currentTime()
        self.label.setText(current_time.toString(Qt.DefaultLocaleLongDate))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
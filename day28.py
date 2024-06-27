import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kalkulator Sederhana')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.layout.addWidget(self.result_display)

        buttons_layout = self.createButtonsLayout()
        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)

    def createButtonsLayout(self):
        buttons_layout = QVBoxLayout()

        # Baris pertama
        row1 = self.createRowLayout(['7', '8', '9', '/'])
        buttons_layout.addLayout(row1)

        # Baris kedua
        row2 = self.createRowLayout(['4', '5', '6', '*'])
        buttons_layout.addLayout(row2)

        # Baris ketiga
        row3 = self.createRowLayout(['1', '2', '3', '-'])
        buttons_layout.addLayout(row3)

        # Baris keempat
        row4 = self.createRowLayout(['0', 'C', '=', '+'])
        buttons_layout.addLayout(row4)

        return buttons_layout

    def createRowLayout(self, buttons):
        row_layout = QHBoxLayout()

        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.buttonClicked)
            row_layout.addWidget(button)

        return row_layout

    def buttonClicked(self):
        button = self.sender()
        button_text = button.text()

        if button_text == '=':
            try:
                result = eval(self.result_display.text())
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText('Error')
        elif button_text == 'C':
            self.result_display.clear()
        else:
            current_text = self.result_display.text()
            new_text = current_text + button_text
            self.result_display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

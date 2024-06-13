import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.layout.addWidget(self.display)

        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+")
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            for text in row:
                button = QPushButton(text)
                button.clicked.connect(self.on_button_click)
                row_layout.addWidget(button)
            self.layout.addLayout(row_layout)

        self.setLayout(self.layout)

    def on_button_click(self):
        sender = self.sender()
        if sender:
            text = sender.text()
            if text == "=":
                expression = self.display.text()
                try:
                    result = str(eval(expression))
                    self.display.setText(result)
                except Exception as e:
                    self.display.setText("Error")
            elif text == "C":
                self.display.clear()
            else:
                self.display.setText(self.display.text() + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

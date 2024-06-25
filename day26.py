import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class DaftarPenumpangBis(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Daftar Penumpang Bis')
        self.setGeometry(100, 100, 400, 300)

        self.label_nama = QLabel('Nama:', self)
        self.input_nama = QLineEdit(self)

        self.label_kursi = QLabel('Nomor Kursi:', self)
        self.input_kursi = QLineEdit(self)

        self.button_tambah = QPushButton('Tambah Penumpang', self)
        self.button_tambah.clicked.connect(self.tambah_penumpang)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_nama)
        self.layout.addWidget(self.input_nama)
        self.layout.addWidget(self.label_kursi)
        self.layout.addWidget(self.input_kursi)
        self.layout.addWidget(self.button_tambah)

        self.setLayout(self.layout)

    def tambah_penumpang(self):
        nama = self.input_nama.text().strip()
        kursi = self.input_kursi.text().strip()

        if not nama or not kursi:
            QMessageBox.warning(self, 'Peringatan', 'Nama dan Nomor Kursi harus diisi!')
            return

        # Menampilkan informasi penumpang (di sini bisa dimodifikasi untuk menyimpan ke file atau database)
        QMessageBox.information(self, 'Informasi', f'Penumpang {nama} dengan nomor kursi {kursi} telah ditambahkan!')

        # Mengosongkan input setelah ditambahkan
        self.input_nama.setText('')
        self.input_kursi.setText('')
        self.input_nama.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DaftarPenumpangBis()
    window.show()
    sys.exit(app.exec_())

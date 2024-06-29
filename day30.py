import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class ContactApp(QWidget):
    def __init__(self):
        super().__init__()
        self.contacts = []  # List untuk menyimpan kontak
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Daftar Kontak')
        self.setGeometry(100, 100, 400, 300)

        # Widget Label dan Line Edit untuk nama kontak baru
        self.label_name = QLabel('Nama:', self)
        self.line_edit_name = QLineEdit(self)

        # Tombol untuk menambahkan kontak baru
        self.button_add = QPushButton('Tambah Kontak', self)
        self.button_add.clicked.connect(self.addContact)

        # Widget untuk menampilkan daftar kontak
        self.list_widget = QListWidget(self)

        # Tombol untuk menghapus kontak yang dipilih
        self.button_delete = QPushButton('Hapus Kontak', self)
        self.button_delete.clicked.connect(self.deleteContact)

        # Layout utama menggunakan QVBoxLayout dan QHBoxLayout
        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.line_edit_name)
        layout.addWidget(self.button_add)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.list_widget)
        h_layout.addWidget(self.button_delete)

        layout.addLayout(h_layout)

        self.setLayout(layout)
        self.show()

    def addContact(self):
        name = self.line_edit_name.text()
        if name:
            self.contacts.append(name)
            self.updateContacts()

    def deleteContact(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            return
        
        item = selected_items[0]
        index = self.list_widget.row(item)
        del self.contacts[index]
        self.updateContacts()

    def updateContacts(self):
        self.list_widget.clear()
        self.list_widget.addItems(self.contacts)
        self.line_edit_name.clear()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Konfirmasi Keluar',
            "Anda yakin ingin keluar dari aplikasi?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ContactApp()
    sys.exit(app.exec_())

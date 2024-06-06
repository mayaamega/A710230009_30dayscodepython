class Mahasiswa:
    def __init__(self, nama, nim, kelas):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas

# Fungsi untuk menambahkan mahasiswa ke dalam daftar
def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    kelas = input("Masukkan kelas mahasiswa: ")
    mahasiswa_baru = Mahasiswa(nama, nim, kelas)
    return mahasiswa_baru

# Fungsi untuk menampilkan daftar mahasiswa
def tampilkan_daftar(daftar_mahasiswa):
    print("Daftar Mahasiswa:")
    for i, mahasiswa in enumerate(daftar_mahasiswa, 1):
        print(f"{i}. Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Kelas: {mahasiswa.kelas}")

# Main program
if __name__ == "__main__":
    daftar_mahasiswa = []  # Inisialisasi daftar mahasiswa kosong
    
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            mahasiswa_baru = tambah_mahasiswa()
            daftar_mahasiswa.append(mahasiswa_baru)
            print("Mahasiswa berhasil ditambahkan.")

        elif pilihan == "2":
            if daftar_mahasiswa:
                tampilkan_daftar(daftar_mahasiswa)
            else:
                print("Daftar mahasiswa kosong.")

        elif pilihan == "3":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
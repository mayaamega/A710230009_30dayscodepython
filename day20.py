class Mahasiswa:
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi
    
    def kartu_mahasiswa(self):
        print(f"===== Kartu Mahasiswa =====")
        print(f"NIM: {self.nim}")
        print(f"Nama: {self.nama}")
        print(f"Angkatan: {self.angkatan}")
        print(f"Program Studi: {self.prodi}")
        print("============================")
    
    def selamat(self):
        print(f"Selamat datang {self.nama} di kampus UMS.")

# Contoh penggunaan kelas Mahasiswa
if __name__ == "__main__":
    # Membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa("A71023", "maya", 2023, " Pendidikan Teknik Informatika")
    mahasiswa2 = Mahasiswa("B23456", "Nishimura Riki", 2023, "Teknik Sipil")
    mahasiswa3 = Mahasiswa("C34567", "Sunghoon", 2023, "Teknik Sipil")
    
    # Memanggil method kartu_mahasiswa() dan selamat() untuk setiap objek
    mahasiswa1.kartu_mahasiswa()
    mahasiswa1.selamat()
    print()
    
    mahasiswa2.kartu_mahasiswa()
    mahasiswa2.selamat()
    print()
    
    mahasiswa3.kartu_mahasiswa()
    mahasiswa3.selamat()

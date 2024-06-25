class Mahasiswa:
    def __init__(self, nama, nim, prodi, angkatan):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.angkatan = angkatan
        self.mata_kuliah = []

    def ambil_mata_kuliah(self, mata_kuliah):
        self.mata_kuliah.append(mata_kuliah)
        print(f"{self.nama} telah mengambil mata kuliah {mata_kuliah}")

    def display_info(self):
        print("Informasi Mahasiswa")
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.prodi}")
        print(f"Angkatan: {self.angkatan}")
        if self.mata_kuliah:
            print("Mata Kuliah yang Diambil:")
            for mata_kuliah in self.mata_kuliah:
                print("- " + mata_kuliah)
        else:
            print("Belum mengambil mata kuliah.")

if __name__ == "__main__":
    mahasiswa1 = Mahasiswa("Nismura Riki", "A710230009", "Teknik Informatika", 2020)
    mahasiswa2 = Mahasiswa("mayamega", "A710230009", "Sistem Informasi", 2019)

    mahasiswa1.ambil_mata_kuliah("Pemrograman Python")
    mahasiswa1.ambil_mata_kuliah("Basis Data")

    mahasiswa2.ambil_mata_kuliah("Algoritma dan Struktur Data")
    mahasiswa2.ambil_mata_kuliah("Pengembangan Web")

    mahasiswa1.display_info()
    print("\n")
    mahasiswa2.display_info()
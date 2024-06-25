class Siswa:
    def __init__(self, nama, usia, kelas):
        self.nama = nama
        self.usia = usia
        self.kelas = kelas

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Usia: {self.usia} tahun")
        print(f"Kelas: {self.kelas}")

class DaftarSiswa:
    def __init__(self):
        self.daftar_siswa = []

    def tambah_siswa(self, siswa):
        self.daftar_siswa.append(siswa)

    def tampilkan_semua_siswa(self):
        print("Daftar Siswa:")
        for siswa in self.daftar_siswa:
            siswa.tampilkan_info()
            print()  # Spasi antar siswa

# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat objek siswa
    siswa1 = Siswa("Jung Hoseok", 15, "XII IPA")
    siswa2 = Siswa("Kim Taehyung", 16, "XII IPS")
    siswa3 = Siswa("Jeon Jungkook", 15, "XI IPA")

    # Membuat daftar siswa
    daftar_siswa = DaftarSiswa()
    daftar_siswa.tambah_siswa(siswa1)
    daftar_siswa.tambah_siswa(siswa2)
    daftar_siswa.tambah_siswa(siswa3)

    # Menampilkan semua siswa
    daftar_siswa.tampilkan_semua_siswa()

class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")

class Mahasiswa(Orang):
    def __init__(self, nama, umur, universitas):
        super().__init__(nama, umur)
        self.universitas = universitas

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kuliah di {self.universitas}")

class Pekerja(Orang):
    def __init__(self, nama, umur, tempat_kerja):
        super().__init__(nama, umur)
        self.tempat_kerja = tempat_kerja

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}, aku kerja di {self.tempat_kerja}")

# Contoh penggunaan:
orang1 = Orang("John", 25)
orang1.kenalan()

mhs = Mahasiswa("Alice", 20, "Universitas XYZ")
mhs.kenalan()

pkj = Pekerja("Bob", 30, "Perusahaan ABC")
pkj.kenalan()

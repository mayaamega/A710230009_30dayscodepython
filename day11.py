class Kalkulator:
    def tambah(self, x, y):
        return x + y

    def kurang(self, x, y):
        return x - y

    def kali(self, x, y):
        return x * y

    def bagi(self, x, y):
        return x / y

calc = Kalkulator()
print("Penjumlahan:", calc.tambah(5, 3))
print("Pengurangan:", calc.kurang(5, 3))
print("Perkalian:", calc.kali(5, 3))
print("Pembagian:", calc.bagi(5, 3))
# Operasi penjumlahan
def tambah(a, b):
    return a + b

# Operasi pengurangan
def kurang(a, b):
    return a - b

# Operasi perkalian
def kali(a, b):
    return a * b

# Operasi pembagian
def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak dapat membagi dengan nol"

# Operasi pangkat
def pangkat(a, b):
    return a ** b

print("Kalkulator Sederhana")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")

pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print("Hasil:", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil:", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil:", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil:", bagi(angka1, angka2))
elif pilihan == '5':
    print("Hasil:", pangkat(angka1, angka2))
else:
    print("Pilihan tidak valid")

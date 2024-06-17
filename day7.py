bulan = int(input("Masukkan nomor bulan (1-12): "))

if bulan in (1, 3, 5, 7, 8, 10, 12):
    print("Jumlah hari: 31")
elif bulan in (4, 6, 9, 11):
    print("Jumlah hari: 30")
elif bulan == 2:
    tahun = int(input("Masukkan tahun: "))
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        print("Jumlah hari: 29 (tahun kabisat)")
    else:
        print("Jumlah hari: 28 (bukan tahun kabisat)")
else:
    print("Nomor bulan tidak valid")

def cek_prima(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

angka = int(input("Masukkan angka: "))
if cek_prima(angka):
    print(angka, "adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")

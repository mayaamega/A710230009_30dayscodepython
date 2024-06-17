def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_ke_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan (C/F): ")

if satuan.upper() == 'C':
    print("Suhu dalam Fahrenheit:", celcius_ke_fahrenheit(suhu))
elif satuan.upper() == 'F':
    print("Suhu dalam Celcius:", fahrenheit_ke_celcius(suhu))
else:
    print("Satuan tidak valid")

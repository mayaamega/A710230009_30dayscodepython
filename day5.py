def maksimum(data):
    max_val = data[0]
    for num in data:
        if num > max_val:
            max_val = num
    return max_val

angka_list = [int(x) for x in input("Masukkan angka dipisahkan dengan spasi: ").split()]
print("Nilai maksimum:", maksimum(angka_list))

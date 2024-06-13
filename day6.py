def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

angka_list = [int(x) for x in input("Masukkan angka dipisahkan dengan spasi: ").split()]
bubble_sort(angka_list)
print("List setelah pengurutan:", angka_list)

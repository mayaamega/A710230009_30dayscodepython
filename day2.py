def sort(lst):
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1 - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        print(">> Iterasi:", j, "List:", lst)

list = [30, 23, 40, 11, 3]

print('Angka yang akan diurutkan:', list)
print('Proses sorting:')
sort(list)
my_list = input("Введите элементы списка: ").split()
for el in range(0, len(my_list)-1, 2):
    my_list[el], my_list[el+1] = my_list[el+1], my_list[el]

print(my_list)

my_list = [7, 5, 3, 3, 2, 2, 1]
x = int(input("Enter positive integer: "))
if x <= 0:
    print("Wrong number. Please, enter positive integer(1,2,3,4,5,6,7,8,9...)")
elif x == 1:
    my_list.append(x)
    print(my_list)
elif x == 2:
    my_list.insert(6, x)
    print(my_list)
elif x == 3:
    my_list.insert(4, x)
    print(my_list)
elif x == 4 or x == 5:
    my_list.insert(2, x)
    print(my_list)
elif x == 6 or x == 7:
    my_list.insert(1, x)
    print(my_list)
elif x >= 7:
    my_list.insert(0, x)
    print(my_list)
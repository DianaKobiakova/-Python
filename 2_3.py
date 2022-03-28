m = int(input("Enter a number of month from 1 to 12:"))
if m < 1 or m > 12:
    print("Wrong number of month. Please, try again!")

month_list = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
season_dict = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Autumn"}
if m == 1 or m == 2 or m == 12:
    print(season_dict.get(1))
elif m == 3 or m == 4 or m == 5:
    print(season_dict.get(2))
elif m == 6 or m == 7 or m == 8:
    print(season_dict.get(3))
elif m == 9 or m == 10 or m == 11:
    print(season_dict.get(4))
    # решила добавить месяцы, как часть практики
if m == 1:
    print(month_list[0])
elif m == 2:
    print(month_list[1])
elif m == 3:
    print(month_list[2])
elif m == 4:
    print(month_list[3])
elif m == 5:
    print(month_list[4])
elif m == 6:
    print(month_list[5])
elif m == 7:
    print(month_list[6])
elif m == 8:
    print(month_list[7])
elif m == 9:
    print(month_list[8])
elif m == 10:
    print(month_list[9])
elif m == 11:
    print(month_list[10])
elif m == 12:
    print(month_list[11])

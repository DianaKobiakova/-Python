my_string = input("Enter string: ")
s = my_string.split(" ")
for i, el in enumerate(s, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}) - {el}")

def my_func(n, s, db, c, e, num):
    print(f"Name - {n}; surname - {s}, year of birth - {db}, city - {c}, email - {e}, phone number - {num}")


my_func(n=input("Enter name: "), s=input("Enter surname: "), db=int(input("Enter year of birth: ")),
        c=input("Enter city: "), e=input("Enter email: "), num=input("Enter phone number: "))


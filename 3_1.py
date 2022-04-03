def my_div(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Please, accept a value not equal to 0!"
    except ValueError:
        return "Enter only number"


print(my_div(int(input("Enter x = ")), int(input("Enter y = "))))

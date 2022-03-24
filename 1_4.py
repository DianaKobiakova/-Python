n = abs(int(input("Enter a positive integer: ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("The maximum digit in a number is: ", max)
        break
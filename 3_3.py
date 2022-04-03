def my_func(v1, v2, v3):
    if v1 >= v3 and v2 >= v3:
        return v1 + v2
    elif v2 < v1 < v3:
        return v1 + v3
    else:
        return v2 + v3


print(
    f"Result: {my_func(v1=int(input('Enter first value: ')), v2=int(input('Enter second value: ')), v3=int(input('Enter third value: ')))}")

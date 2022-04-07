def sal():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка в hrn: '))
        bonus = int(input('Премия в hrn: '))
        res = time * salary + bonus
        print(f'Зарплата сотрудника: {res}')
    except ValueError:
        return print('Not a number')


sal()

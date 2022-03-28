a = int(input("Enter the result of running on the first day in km: "))
b = int(input("Enter the desired result in km: "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"You`ll achieve the desired result on the %.d day" % result_days)
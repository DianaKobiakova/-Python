revenue = float(input("Enter the company revenue: "))
costs = float(input("Enter the company costs: "))
if revenue > costs:
    print(f"The company is operation at a profit. Return on revenue is {revenue / costs:.2f}")
    employees = int(input("Enter the number of employees: "))
    print(f"Profit per employee amounted to {revenue / employees:.2f}")
elif revenue == costs:
    print("The company is running at zero")
else:
    print("The company is operation at a loss")
try:
    num1 = float(input("Insert the number that will be divided: "))
    num2 = float(input("Insert the number that will divide: "))
    result = num1/num2
except ZeroDivisionError:
    print("Division by 0 not allowed.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"{num1} / {num2} = {result}")
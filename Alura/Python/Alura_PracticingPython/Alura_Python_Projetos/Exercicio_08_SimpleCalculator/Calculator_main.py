def calculator(num1,op,num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if not num2 == 0:
            return num1 / num2
        else:
            raise ZeroDivisionError
    else:
        raise TypeError
        
try:
    num1 = float(input("Insert the first number: "))
    op = input("Choose a operation (+, -, *, /): ")
    num2 = float(input("Insert the second number: "))
    
    result = calculator(num1,op,num2)
    print(f"Result: {result}")

except ValueError:
    print(f"Error: Invalid input. Insert numbers only.")
except TypeError:
    print("Error: Choose only between the operations: ( +, -, *, / )")
except ZeroDivisionError:
    print("Error: Division by Zero not allowed.")
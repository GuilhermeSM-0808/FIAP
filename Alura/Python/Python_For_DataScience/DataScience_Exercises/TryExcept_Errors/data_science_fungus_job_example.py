## Exercise 07

pressure = [100, 120, 140, 160, 180]
temperatures = [20, 25, 30, 35, 40]

def correlation(data01,data02):
    result = []
    if len(data01) != len(data02):
        raise IndexError("The data lists are of different lengths.")
    elif 0 in data02:
        raise ZeroDivisionError 
    else:
        for v in range(len(data01)):
            result.append(round((data01[v]/data02[v]),4))
    return result

try:
    result = correlation(pressure,temperatures)
    print(result)
except IndexError as e:
    print("Error:", e)
except ZeroDivisionError:
    print("Error: Zero division not allowed.")
def area(side, height):
    try:
        area = float(side) * float(height)
        return area
    except:
        print("Invalid input.")

a, b = (input("Insert the length of the side and height of the shape, separated by a comma ',': ").split(','))

print(area(a,b))
val_01 = int(input("Insert a whole number N°1: "))
val_02 = int(input("Insert a whole number N°2: "))
val_03 = int(input("Insert a whole number N°3: "))


if val_01 > val_02 and val_01 > val_03:
    print(f"N°1: {val_01} is the biggest Number")
elif val_02 > val_01 and val_02 > val_03:
    print(f"N°2: {val_02} is the biggest Number")
elif val_03 > val_01 and val_03 > val_02:
    print(f"N°3: {val_03} is the biggest Number")

if val_01 == val_02 or val_01 == val_03 or val_02 == val_03:
    print("There are repeated numbers.")
print(f"N°1: {val_01}")
print(f"N°2: {val_02}")
print(f"N°3: {val_03}")
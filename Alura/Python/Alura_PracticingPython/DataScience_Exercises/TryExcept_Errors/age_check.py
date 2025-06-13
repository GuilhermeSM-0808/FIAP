ages = {"Foo": 32, "bar": 21, "Qux":27}

try:
    check = input("Insert the name of the person you would to know the age of: ")
    age = ages[check]
except KeyError:
    print("Person not registered.")
else:
    print(f"{check} is {age} years old.")
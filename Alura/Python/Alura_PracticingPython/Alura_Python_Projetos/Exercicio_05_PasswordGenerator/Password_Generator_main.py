import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
digits = "0123456789"
special = "!@#$%&*"


def password_generator():
    password = []
    password.append(upper[random.randint(0,(len(upper) -1))])
    password.append(lower[random.randint(0,(len(lower) -1))])
    password.append(digits[random.randint(0,(len(digits) -1))])
    password.append(special[random.randint(0,(len(special) -1))])
    for i in range(4,12):
        group = random.choice([upper,lower,digits,special])
        password.append(group[random.randint(0,(len(group) -1))])
    random.shuffle(password)
    password = "".join(password)
    return password

print(password_generator())
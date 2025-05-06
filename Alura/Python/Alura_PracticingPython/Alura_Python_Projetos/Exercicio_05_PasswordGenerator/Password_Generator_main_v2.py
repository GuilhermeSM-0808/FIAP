import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
digits = "0123456789"
special = "!@#$%&*"


def password_generator():
    password = ""
    for i in range(0,12):
        group = random.choice([upper,lower,digits,special])
        password += (group[random.randint(0,(len(group) -1))])
    check_u = 0
    check_l = 0
    check_d = 0
    check_s = 0
    for p in password:
        if p in upper:
            check_u += 1
        if p in lower:
            check_l += 1
        if p in digits:
            check_d += 1
        if p in special:
            check_s += 1
    if check_s == 0 or check_d == 0 or check_l == 0 or check_u == 0:
        return password_generator()
    return password

print(password_generator())
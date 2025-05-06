import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
digits = "0123456789"
special = "!@#$%&*"

def contains_at_least_one(check, group1, group2, group3, group4):
    return (any(c in check for c in group1) and any(c in check for c in group2) and any(c in check for c in group3) and any(c in check for c in group4))

def password_generator():
    password = ""
    for i in range(0,12):
        group = random.choice([upper,lower,digits,special])
        password += (group[random.randint(0,(len(group) -1))])
    if not contains_at_least_one(password, upper, lower, digits, special):
        return password_generator()
    return password

print("Generated password:", password_generator())
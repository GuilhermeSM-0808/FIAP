withdraw_values = {
    "100":0,
    "50":0,
    "20":0,
    "10":0,
    "5":0,
    "2":0
}


def atm_output(amount):
    if amount / 100 >= 1:
        withdraw_values["100"] += 1
        amount -= 100
        return amount
    elif amount / 50 >= 1:
        withdraw_values["50"] += 1
        amount -= 50
        return amount
    elif amount / 20 >= 1:
        withdraw_values["20"] += 1
        amount -= 20
        return amount
    elif amount / 10 >= 1:
        withdraw_values["10"] += 1
        amount -= 10
        return amount
    elif amount / 5 >= 1 and (amount - 5) % 2 == 0:
        withdraw_values["5"] += 1
        amount -= 5
        return amount
    elif amount / 2 >= 1:
        withdraw_values["2"] += 1
        amount -= 2
        return amount
        


try:
    withdraw_amount = int(input("Insert the amount you would like to withdraw: "))
    if withdraw_amount <= 0:
        raise ZeroDivisionError
    if withdraw_amount % 2 == 0 or withdraw_amount % 5 == 0 or (withdraw_amount - 2) % 5 == 0 or (withdraw_amount - 4) % 5 == 0:
        while withdraw_amount > 1:
            withdraw_amount = atm_output(withdraw_amount)
        print("Banknotes to be withdrawn: ")
        for count in withdraw_values:
            print(f"{withdraw_values[count]} note of ${count}")
    else:
        print("Invalid input. The number must be divisable by 2 or 5.")
except ValueError:
    print("Invalid input. Insert only whole numbers.")
except ZeroDivisionError:
    print("Invalid input. Input must be greater than Zero.")
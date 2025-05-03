## Initial Code

# bill_amount = float(input("Insert the bill amount: "))
# tip_percentage = float(input("Insert the tip amount in percetage you would like to give: ")) / 100
# tip_amount = bill_amount * tip_percentage
# total_amount = tip_amount + bill_amount
# print(f"Tip amount is: R${tip_amount}")
# print(f"Bill Total: R${total_amount}")

from tip_calculator import tip_total

try:
    bill_amount = float(input("Insert the bill amount: "))
    tip_percentage = float(input("Insert the tip amount in percetage you would like to give: ")) / 100
    total_amount, tip_amount = tip_total(bill_amount, tip_percentage)
    print(f"Tip amount is: R${tip_amount:.2f}")
    print(f"Bill Total: R${total_amount:.2f}")
except ValueError:
    print("Erro: Insira apenas digitos.")
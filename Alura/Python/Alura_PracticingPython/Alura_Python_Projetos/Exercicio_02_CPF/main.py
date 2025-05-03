import re

CPF_pattern = r'\d{11}'

CPF_input = input("Insert your CPF number: ")
CPF_input = CPF_input.replace(".","").replace("-","")

if re.match(CPF_pattern, CPF_input) and len(CPF_input) == 11:
    print("Valid CPF.")
else:
    print("Invalid input.")
    if len(CPF_input) != 11:
        print("CPF numbers have exactly 11 digits.")
    if re.search(r'\D+', CPF_input):
        print("CPF is composed of digits only.")    
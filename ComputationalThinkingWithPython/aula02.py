### Extrair codigo de cada Exemplo e Exercicios, rodalos individualmente

##Ex.1
#Inputs
variavel_A = 20
variavel_B = 20

#Outputs
print(f'Valor da variavel A eh {variavel_A}')
print(f'Valor da variavel B eh {variavel_B}')

#Conditions

if variavel_A == variavel_B:
    print('A eh igual a B')
elif variavel_A > variavel_B:
    print('A eh maior que B')
else:
    print('B eh maior que A')

##Ex.2
#User Input

a = float(input("Insira Valor de A: "))
b = float(input("Insira Valor de B: "))

if a == b:
    print('A eh igual a B')
elif a > b:
    print('A eh maior que B')
else:
    print('B eh maior que A')

##Ex.3
#User Login

usuario = str(input("Digite um caractere ou palavra: "))
senha = int(input("Digite uma senha: "))

print(usuario)
print(senha)

##Ex.4
#User Input X Constant variables

x = float(input("Digite valor de X: "))

resultado = (2*x) + 10

print(resultado)

##Ex.5
#Algorithym to calculate the following math equations

##Exercicio 5.1
x = float(input("De um valor para X: "))

R = (10*x)**2 + (2*x) - 2

print(R)

##Exercicio 5.2
x = float(input("De um valor para X: "))
y = float(input("De um valor para Y: "))

R = (15*x)**2 + (3*y) + 5

print(R)

##Exercicio 5.3
x = float(input("De um valor para X: "))
y = float(input("De um valor para Y: "))
z = float(input("De um valor para Z: "))

R = (10*x)**2 + (4*y)**2 - (2*z)**2

print(R)

#tudo junto
x = float(input("De um valor para X: "))
y = float(input("De um valor para Y: "))
z = float(input("De um valor para Z: "))

R1 = (10*x)**2 + (2*x) - 2
R2 = (15*x)**2 + (3*y) + 5
R3 = (10*x)**2 + (4*y)**2 - (2*z)**2

print(R1)
print(R2)
print(R3)

##Ex.7

import sympy as sp

x = sp.symbols('x')
print(x)

a = 1
b = -3
c = 2

equation = a*x**2 + b*x + c

solution = sp.solve(equation, x)
print(solution)

#Operation with Strings

nome = 'Albert'
sobrenome = 'Einstein'

print(nome)
print(sobrenome)

nome_completo = nome + sobrenome
print(nome_completo)

nome_comp = nome + " " + sobrenome
print(nome_comp)

##Exercicio pratico 8

#part 1
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

R1 = a + b + c
R2 = a - b + c
R3 = (a**2 + 2*b - 5.1*c)
R4 = a + b == c
R5 = c - a == b
R6 = a + c == b - c

print(R1)
print(R2)
print(R3)
print(R4)
print(R5)
print(R6)

#part 2

S1 = 2500
S2 = 3500
S3 = 5000

im1 = S1*0.1
im2 = S2*0.15
im3 = S3*0.25

re1 = S1 - im1
re2 = S2 - im2
re3 = S3 - im3

print(f"Salario: ${S1} reais. Imposto a ser pago: ${im1} reais. Salario apos imposto: ${re1} reais.")
print(f"Salario: ${S2} reais. Imposto a ser pago: ${im2} reais. Salario apos imposto: ${re2} reais.")
print(f"Salario: ${S3} reais. Imposto a ser pago: ${im3} reais. Salario apos imposto: ${re3} reais.")

#part 3

Email01 = str(input("01 Insert your email: "))
Pass01 = str(input("01 Insert your Password: "))
TwoFact01 = str(input("01 Insert your Two Factor authenticator code: "))

Email02 = str(input("02 Insert your email: "))
Pass02 = str(input("02 Insert your Password: "))
TwoFact02 = str(input("02 Insert your Two Factor authenticator code: "))

print(f"User01 email: {Email01}")
print(f"User01 password: {Pass01}")
print(f"User01 Twofactor autheticator code: {TwoFact01}")
print(f"User02 email: {Email02}")
print(f"User02 password: {Pass02}")
print(f"User02 Twofactor autheticator code: {TwoFact02}")
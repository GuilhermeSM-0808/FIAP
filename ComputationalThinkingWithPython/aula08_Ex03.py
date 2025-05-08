a = float(input("Insert the value of A of equation Ax + B: "))
b = float(input("Insert the value of B of equation Ax + B: "))
c = float(input("Insert the value of C of equation Cx + D: "))
d = float(input("Insert the value of D of equation Cx + D: "))
# x = float(input("Insert the value of X: "))

def quadrado(n):
    return n*n

def second_degree_equation(a,b,c,d):
    A = a*c
    B = a*d
    C = b*c
    D = b*d

    E = B + C

    x1 = (((-E) + (((E**2)-4*A*D)**(1/2)))/(2*A))
    x2 = (((-E) - (((E**2)-4*A*D)**(1/2)))/(2*A))

    equation = f"({A})x^2 + ({E})x + ({D})"
    resultado1 = (A * quadrado(x1) + E * x1 + D)
    resultado2 = (A * quadrado(x2) + E * x2 + D)
    return equation, x1, x2, resultado1, resultado2

equation, x1, x2, resultado1, resultado2 = second_degree_equation(a,b,c,d)

print(f"\n{equation}\n")    
print(f"Valores de X: {x1:.4f} e {x2:.4f}")    
print(f"\nResultado 01:{resultado1:.4f}")    
print(f"Resultado 02:{resultado2:.4f}\n")    
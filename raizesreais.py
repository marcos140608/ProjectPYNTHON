A=float(input("digite o valor do coeficiente A:"))
B=float(input("digite o valor do coeficiente B:"))
C=float(input("digite o valor do coeficiente C:"))
delta=(B**2)-(4*A*C)
x1=-B+delta**0.5/2*A
x2=B-delta**0.5/2*A
print(f"o valor das raizes reais é: {x1} e {x2}")
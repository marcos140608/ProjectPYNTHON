horastrabalhada=float(input("quantas horas trabalhada:"))
valorporhora=float(input("qual é o valor por hora:"))
percentual=float(input("digite o percentual de desconto:"))
dependentes=float(input("digite o numero de dependentes:"))
salariobruto=horastrabalhada*valorporhora
salarioliquido=salariobruto-(salariobruto*percentual/100) + dependentes*100
print(f"o salario a receber sera: {salarioliquido:.2f}")

salarioB = float(input("Informe o salário bruto: "))
provento = float(input("Valor de proventos: "))

if(salario <= 5000):
    print("Salário líquido:", (salarioB+provento*5)/100)
else:
    print("Salário líquido:", (salarioB+provento*10)/100)

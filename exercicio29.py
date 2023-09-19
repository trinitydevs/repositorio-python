salarioB = float(input("Informe o salário bruto: "))
provento = float(input("Valor de proventos: "))

desconto5 = (salarioB*5)/100
desconto10 = (salarioB*10)/100

if(salarioB <= 5000):
    print("Salário líquido: R$", (salarioB + provento) - desconto5)
else:
    print("Salário líquido: R$", (salarioB + provento) - desconto10)

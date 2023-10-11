funcionario = True
salario = []
abono = []
while funcionario != 0:
    valor = float(input("Informe o salário: "))
    if valor == 0:
        break
    salario.append(valor)

print('\nSalário    - Abono')

for i in range(len(salario)):
    percentual = salario[i] * 0.20
    if (percentual <= 100):
        percentual = 100
    print('R${:>8.2f} - R${:>8.2f}'.format(salario[i],percentual))
    abono.append(percentual)

valMin = abono.count(100)
print(f"Foram processados {len(salario)} colaboradores")
print(f"Valor mínimo pago a {valMin} colaboradores ")
print(f"Maior valor de abono pago: R$ {max(abono):.2f}")
print(f"Total gasto com abonos: R$ {sum(abono):.2f}")



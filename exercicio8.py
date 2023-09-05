quilowatts = int(input("Digite o total gasto em quilowatts:"))
quilowattsPreco = int(1320/7)
unidadeQuilowatts = int(quilowattsPreco/100)
print("O quilowatts equivale a:" , "R$", unidadeQuilowatts)
print("O total a pagar é de: R$", unidadeQuilowatts * quilowatts)
valorTotal = (unidadeQuilowatts * quilowatts)/10
print("Valor a ser pago com desconto de 10%: ", unidadeQuilowatts * quilowatts - valorTotal)
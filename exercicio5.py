valor = float(input("Informe o valor: "))
taxa = float(input("Informe a taxa: "))
tempo = float(input("Informe o tempo em horas: "))

prestacao = valor + (valor*(taxa/100) * tempo)

print("A prestação é de R$",prestacao)
print("Nos informe as dimensões do reservatório ")
#DIMENSÕES
altura = float(input("Informe a altura: "))
largura = float(input("Informe a largura: "))
comprimento = float(input("Por último, informe o comprimento: "))

#CONSUMO
print("Agora, nos informe o consumo médio diario ")
litros = float(input("Quantidade de litro diário: "))
volume = altura*largura*comprimento

reservatorioTotal = volume*1000

#CAPACIDADE
print("Capacidade total do reservátorio: ",  reservatorioTotal,"l")

autonomia = reservatorioTotal/litros
#AUTONOMIA
print("A autonomia do reservatório, em dias, é:", "{:.0f}".format(autonomia),"dias")

if(autonomia < 2):
    print("Consumo elevado")
elif(autonomia == 2 and autonomia <= 7):
    print("Consumo moderado")
else:
    print("Consumo reduzido")



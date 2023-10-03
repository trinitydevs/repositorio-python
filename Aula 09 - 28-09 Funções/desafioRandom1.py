import random
numeros = []
for i in range(75):
    sorteio = str(input("Digite enter para gerar um número (0 para sair): "))
    if(sorteio == "0"):
        break
    elif(sorteio == ""):
        valor = random.randint(1, 75)
        if valor not in numeros:
            numeros.append(valor)
        print(numeros[i])
        print(numeros)
print(f"Números sorteados: {numeros}")
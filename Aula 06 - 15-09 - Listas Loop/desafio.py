lista = [0]
pares = []
impares = []
for contagem in range(5):
    numero = int(input("Digite um número (zero para sair): "))
    lista.append(numero)
    if(numero%2 == 0):
        print("par")
        pares.append(numero)
    elif(numero == 0):
        break
    else:
        print("impar")
        impares.append(numero)
soma = sum(lista)
print("Números pares: ",sorted(pares, key=int))
print("Números ímpares: ",sorted(impares, key=int, reverse=True))
print("SOMA: ",soma)
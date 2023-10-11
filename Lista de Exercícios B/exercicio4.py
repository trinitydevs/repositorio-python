numeros = []
for i in range(100):
    valores = int(input("Informe uma nota: "))
    numeros.append(valores)
    if(valores == -1):
        break;
total = sum(numeros)-1
media = sum(numeros)/1
numeros.pop()
print("Total de valores lidos: ", len(numeros))
print("Valores inversos:")
for x in reversed(numeros):
    print(x)
print("")





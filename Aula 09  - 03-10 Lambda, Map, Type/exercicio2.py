numeros = []
for i in range(10):
    numero = int(input("Informe o número: "))
    numeros.append(numero)
listaImpar = list(filter(lambda x: x % 2 != 0, numeros))
listaPar = list(filter(lambda x: x % 2 == 0, numeros))

#retorna a lista de números ímpares
print("\n\nPar = ", listaPar,
"\n\nÍmpar = ", listaImpar)
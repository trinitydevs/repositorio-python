#L4E04
somaPar = []
for contagem in range(100):
    numero = int(input("Digite um número: (666 para sair)"))
    if(numero == 666):
        break
    elif(numero%2 == 0):
        somaPar.append(numero)
    
total = sum(somaPar)
print(f'Soma dos números pares: {total}')
    
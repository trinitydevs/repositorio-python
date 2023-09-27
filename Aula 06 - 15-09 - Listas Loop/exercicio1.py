lista = []
for contagem in range(5):
    numero = int(input("Digite um número (zero para sair): "))
    if(numero != 0):
       lista.append(numero)
    else:
        break
print("Soma = ",lista[0]+lista[1]+lista[2]+lista[3]+lista[4])
print("Multiplicação:",lista[0]*lista[1]*lista[2]*lista[3]*lista[4])

if lista[0] < lista[1] and lista[0] < lista[2] and lista[0] < lista[3] and lista[0] < lista[4]:
        print("Menor valor: ",lista[0])
elif lista[1] < lista[0] and lista[1] < lista[2] and lista[1] < lista[3] and lista[1] < lista[4]:
        print("Menor valor: ",lista[1])
elif lista[2] < lista[0] and lista[2] > lista[1] and lista[2] < lista[3] and lista[2] < lista[4]:
        print("Menor valor: ",lista[2])
elif lista[3] < lista[0] and lista[3] < lista[1] and lista[3] < lista[2] and lista[3] < lista[4]:
        print("Menor valor: ",lista[3])
elif lista[4] < lista[0] and lista[4] < lista[1] and lista[4] <lista[2] and lista[4] < lista[3]:
        print("Menor valor: ",lista[4])

if lista[0] > lista[1] and lista[0] > lista[2] and lista[0] > lista[3] and lista[0] > lista[4]:
        print("Maior valor: ",lista[0])
elif lista[1] > lista[0] and lista[1] > lista[2] and lista[1] > lista[3] and lista[1] > lista[4]:
        print("Maior valor: ",lista[1])
elif lista[2] > lista[0] and lista[1] and lista[2] > lista[3] and lista[2] > lista[4]:
        print("Maior valor: ",lista[2])
elif lista[3] > lista[0] and lista[3] >  lista[1] and lista[3] >  lista[2] and lista[3] >  lista[4]:
        print("Maior valor: ",lista[3])
elif lista[4] > lista[0] and lista[4] > lista[1] and lista[4] > lista[2] and lista[4] > lista[3]:
        print("Maior valor: ",lista[4])
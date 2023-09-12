numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))

if(numA !=0 and numB == 0):
    print("Impossível dividir",numA,"por 0")
elif(numA%numB == 0):
    print(numA,"é divisível por",numB)
else:
    print(numA,"não é divisível por",numB)





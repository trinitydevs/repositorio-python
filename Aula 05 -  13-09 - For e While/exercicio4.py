contagem = 0
armazenamentoM = 0
armazenamentoH = 0
totalM = 0
totalH = 0

for contagem in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sexo = str(input("Informe o sexo: digite M para mulher e H para homem! "))
    idade = int(input("Digite a sua idade: "))
    if(sexo == "M" or sexo == "m"):
        print("Mulher!")
        armazenamentoM += idade
        totalM += 1
    elif(sexo == "H" or sexo == "h"):
        print("Homem!")
        armazenamentoH += idade
        totalH += 1
    else:
        print("Caractere inválido!")
        break
    
print("Idade média das Mulheres:", armazenamentoM/totalM)
print("Idade média dos Homens:", armazenamentoH/totalH)
print("Idade média do grupo: ", (armazenamentoM+armazenamentoH)/(totalM+totalH))


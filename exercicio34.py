numAluno = int(input("Digite o número de identificação do aluno: "))
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
mediaEx = int(input("Informe a média dos exercícios: "))


mediaA = (n1 + n2*2 + n3 *3 + mediaEx)/7

if(mediaA >= 9):
    print("N° Identificação: ", numAluno)
    print("Conceito A: APROVADO")
    print("MA =", mediaA)
elif(mediaA >= 7.5 and mediaA < 9):
    print("N° Identificação: ", numAluno)
    print("Conceito B: APROVADO")
    print("MA =", mediaA)
elif(mediaA >= 6 and mediaA < 7.5):
    print("N° Identificação: ", numAluno)
    print("Conceito C: APROVADO")
    print("MA =", mediaA)
elif(mediaA >= 4 and mediaA < 6):
    print("N° Identificação: ", numAluno)
    print("Conceito D: REPROVADO")
    print("MA =", mediaA)
else:
    print("N° Identificação: ", numAluno)
    print("Conceito E: REPROVADO")
    print("MA =", mediaA)

codAluno = int(input("Digite o código do aluno: "))
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

if(n1 > n2 and n1 > n3):
    mediaP = (n1*4+n2*3+n3*3)/10
elif(n2 > n1 and n2 > n3):
    mediaP = (n2*4+n1*3+n3*3)/10
elif(n3 > n2 and n3 > n1):
    mediaP = (n2*3+n1*3+n3*4)/10
elif(n1 > n3 and n1 == n2):
    mediaP = (n1*4+n2*3+n3*3)/10
elif(n3 > n2 and n3 == n2):
    mediaP = (n1*3+n2*4+n3*3)/10
else:
    mediaP = (n1*4+n2*3+n3*3)/10
    print(mediaP)

if(mediaP >= 5):
    print("Código:",codAluno)
    print("NOTA 1: ",n1)
    print("NOTA 2: ",n2)
    print("NOTA 3: ",n3)
    print("MÉDIA:",mediaP,". Aprovado!")
else:
    print("Código:",codAluno)
    print("NOTA 1: ",n1)
    print("NOTA 2: ",n2)
    print("NOTA 3: ",n3)
    print("MÉDIA:",mediaP,". Reprovado!")
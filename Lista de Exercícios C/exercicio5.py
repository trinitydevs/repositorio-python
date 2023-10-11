aluno = {"nome": ['', '', ''], "notas": ['', '', '']}
nomes = []
notas = []
val = 1
media = []
maior = None

while True:
    nome = str(input("Informe o nome (0 para sair): "))
    if(nome == "0"):
        break
    nomes.append(nome)
    aluno['nome'] = nomes
    for i in range(2):
        nota = float(input(f"Digite a {i} nota: "))
        notas.append(nota)
        aluno['notas'] = notas

print(aluno)
for y in range(len(aluno['nome'])):
    media += {aluno['notas'][y] + aluno['notas'][y+val]/2}
    print(f"Média {(aluno['nome'][y])}: {media[y]} ")
    y += 1
for item in media:
    if(maior is None or item > maior):
        maior = item 
print(f"O aluno com maior nota é {aluno['nome'][media.index(maior)]} com nota {maior}")
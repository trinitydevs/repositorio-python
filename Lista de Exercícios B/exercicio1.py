alunos = 30
idades = []
alturas = []
mediaAltura = 0
abaixoMedia = 0

for contagem in range(alunos):
    idades.append(int(input(f"Digite a idade do aluno {contagem+1}: ")))
    altura = int(input(f"Digite a altura{contagem+1}: "))
    alturas.append(altura)
    mediaAltura += altura

mediaAltura /= alunos

for contagem in range(alunos):
    if(idades[contagem] > 13):
        if(alturas[contagem] < mediaAltura):
            abaixoMedia += 1

print(f"{abaixoMedia} alunos com mais de 13 anos têm altura abaixo da média")

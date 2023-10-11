#L4E09
v#L4E09
votos = ['1 - Branco', '2 - Nulo', '3 - Kiko', '4 - Chaves', '5 - Chiquinha']
branco = 0
nulo = 0
kiko = 0
chaves = 0
chiquinha = 0
for contagem in range(100):
    opcao = int(input(f'Vote em um candidato: {votos}'))
    if(opcao == 1):
        branco += 1
    elif(opcao == 2):
        nulo += 1
    elif(opcao == 3):
        kiko += 1
    elif(opcao == 4):
        chaves += 1
    elif(opcao == 5):
        chiquinha += 1
    elif(opcao == 666):
        break
    else:
        print("Número invalido!")
print(f'Branco = {branco}\n Nulo = {nulo} \n Kiko = {kiko} \n Chaves = {chaves} \n Chiquinha = {chiquinha}\n')
    
    
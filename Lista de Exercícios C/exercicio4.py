mouses = []
opcoes = ['1 - Necessita da Esfera', '2 - Necessita de limpeza', '3 - Necessita troca do cabo ou conector', '4 - Quebrado ou inutilizado']
estado = [0, 0, 0, 0]
while True:
    identificacao = str(input("Digite a identificação do mouse (0 para encerrar): "))
    if(identificacao == "0"):
        break
    mouses.append(identificacao)
    print(opcoes)
    resposta = int(input(" "))
    estado.append(resposta)
opcao1 = estado.count(1)
opcao2 = estado.count(2)
opcao3 = estado.count(3)
opcao4 = estado.count(4)

total = opcao1+opcao2+opcao3+opcao4
print("SITUAÇÃO  - QUANTIDADE   -  PERCENTUAL")
print(f"{opcoes[0]}: {opcao1} - {(opcao1/total)*100:.0f}%")
print(f"{opcoes[1]}: {opcao2} - {(opcao2/total)*100:.0f}%")
print(f"{opcoes[2]}: {opcao3} - {(opcao3/total)*100:.0f}%")
print(f"{opcoes[3]}: {opcao4} - {(opcao4/total)*100:.0f}%")




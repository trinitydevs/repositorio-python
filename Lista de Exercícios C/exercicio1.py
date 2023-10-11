sistemaOperacional = ['1 - Windows Server', '2 - Unix', '3 - Linux', '4 - Netware', '5 - Mac OS', '6 - Outro']
opcao = 0
valores = []
lista = []
totalVotos = []
valor = 0

for i in range(100):
    resposta = int(input(f"\nDada a sua preferência de melhor Sistema Operacional, escolha as opcões (0 para sair): {sistemaOperacional}"))
    valores.append(resposta)
    if(resposta == 0):
        break
opcao1 = valores.count(1)
opcao2 = valores.count(2)
opcao3 = valores.count(3)
opcao4 = valores.count(4)
opcao5 = valores.count(5)
opcao6 = valores.count(6)
totalVotos.append(opcao1)
totalVotos.append(opcao2)
totalVotos.append(opcao3)
totalVotos.append(opcao4)
totalVotos.append(opcao5)
totalVotos.append(opcao6)

total = opcao1+opcao2+opcao3+opcao4+opcao5+opcao6
windows = (opcao1/total)*100
unix = (opcao2/total)*100
linux = (opcao3/total)*100
netware = (opcao4/total)*100
mac = (opcao5/total)*100
outro = (opcao6/total)*100

lista.append(windows)
lista.append(unix)
lista.append(linux)
lista.append(netware)
lista.append(mac)
lista.append(outro)

for contagem in range(6):
    print(f'Total de votos para {sistemaOperacional[0+valor]} = {totalVotos[0+valor]} PERCENTUAL = {lista[0+valor]:.2f}%')
    valor +=1
    
    



    
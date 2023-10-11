contadorSim = 0
contadorNao = 0
perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
for perguntar in perguntas:
    resposta = str(input(perguntar))
    if(resposta == "sim" or resposta == "SIM" or resposta == "Sim"):
        contadorSim += 1
    else:
        contadorNao += 1
if(contadorSim == 2):
    print("Classificação: Suspeito!")
elif(contadorSim > 2 and contadorSim <5):
    print("Classificação: Cúmplice!")
elif(contadorSim == 5):
    print("Classificação: Assassino!")
else: 
    print("Inocente!")
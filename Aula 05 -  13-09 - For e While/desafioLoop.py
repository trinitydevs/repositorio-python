numero = int(input("Digite um número para ver a tabuada correspondente: "))
contagem = 1
respostaCerta = 0
respostaIncorreta = 0
for contagem in range(10):
    print(numero,"x",contagem+1,"=")
    resposta = int(input(""))      
    respostaCorreta = numero*(contagem+1)
    if(resposta == respostaCorreta):
        print("Você acertou!")
        respostaCerta +=1
    else:
        print("Você errou, a resposta é:", respostaCorreta)
        respostaIncorreta +=1
print("Total de acertos: ", respostaCerta)
print("Total de erros: ", respostaIncorreta)

    

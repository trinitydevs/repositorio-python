golTimeUm = int(input("Informe o número de gols do time I: "))
golTimeDois = int(input("Informe o número de gols do time II: "))

if(golTimeUm > golTimeDois):
    print("O time I venceu de ", golTimeUm ,"a", golTimeDois)
elif(golTimeDois > golTimeUm):
    print("O time II venceu de ", golTimeDois ,"a", golTimeUm)
else: 
    print("O jogo deu empate!")

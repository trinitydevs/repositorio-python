lista = []
palavra1 = 0
palavra2 = 0
palavra3 = 0
palavra4 = 0
palavra5 = 0
for contagem in range(5):
    palavra = str(input("Informe uma palavra (zero para sair): "))
    if(palavra != "0" and palavra != ""):
       lista.append(palavra)
       print("Palavras adicionadas: ",lista)
       

    else:
        print("Palavras adicionadas: ",lista)
        resposta = str(input("Informe a palavra e veja o número de ocorrências dela: "))
        string = lista
        substring = resposta
        count = string.count(substring)
        print("Total de ocorrências da palavra: ", count)
                
resposta = str(input("Informe a palavra e veja o número de ocorrências dela: "))
string = lista
substring = resposta
count = string.count(substring)
print("Total de ocorrências da palavra: ", count)
    


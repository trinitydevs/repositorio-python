lista = []
for contagem in range(5):
    numero = input("Digite um número (zero para sair): ")
    lista += numero
    if(numero == "0"):
        break
if __name__ == '__main__':
	repeticao = {x for x in lista if lista.count(x) > 1}
	print("Números que se repetem: ",repeticao)
nRepeticao = {i for i in lista if lista.count(i) == 1}
print("Números que não se repetem: ",nRepeticao) 




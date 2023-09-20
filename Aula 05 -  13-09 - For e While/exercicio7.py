numero = int(input("Digite um número: "))
resposta = 1
for contagem in range(1, numero + 1):
    resposta *= contagem
print(resposta)
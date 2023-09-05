numero = input("Digite os três digitos da conta corrente: ")
juncao = numero[2]+numero[1]+numero[0]
juncao = int(juncao)
numero = int(numero)

total = numero+juncao
print("Soma dos números inversos: ", total)
total = str(total)
print(total)
numeroUm = total[0]
numeroDois = total[1]
numeroTres = total[2]

numeroUm = int(numeroUm)
numeroDois = int(numeroDois)
numeroTres = int(numeroTres)

soma = (numeroUm*1)+(numeroDois*2)+(numeroTres*3)
print("Multiplicação de dígitos pela posição: ", soma)

soma = str(soma)
verificador = soma[1]

print("DIGITO VERIFICADOR: ", verificador)
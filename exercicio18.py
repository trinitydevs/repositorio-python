#Definindo a quantida de fitas
qtdFitas = int(input("Informe a quantidade de fitas: "))

#Definindo o valor a  ser cobrado do aluguel
valorAluguel = float(input("Informe o aluguel da fita de vídeo: "))

#Um terço da quantidade das fitas é alugada mensalmente
mesFitas = (qtdFitas/3) * valorAluguel
print("O faturamento anual da locadora é de: R$", mesFitas*12)

#Multa de 10% sobre o valor do aluguel caso haja atraso.
valorMulta = valorAluguel*10/100

#Valor ganho de multas por mês
mesFitass = qtdFitas/3
decimoFitas = mesFitass/10
print("Valor das multas mensal: R$", decimoFitas*valorMulta)

#Total de fitas ao final de 1 ano
#2% do total de fitas
doisPorcFitas = qtdFitas*2/100
#Qtd fitas total
fitasTotal = qtdFitas - doisPorcFitas
decimoTotal = fitasTotal/10
print("Total de fitas ao final de 1 ano:", fitasTotal + decimoTotal)
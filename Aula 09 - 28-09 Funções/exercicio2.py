#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
quantia = float(input("Informe o custo: "))
porcentagem = int(input("Informe o valor do imposto sobre o produto: "))
print(f"Preço do produto: R${quantia:.2f}")

def somaImposto(taxaImposto = None, valor = None):
    global quantia
    global porcentagem
    valor = (quantia*porcentagem)/100
    taxaImposto = quantia + valor
    return taxaImposto
print(f"Valor total a ser pago: R${somaImposto():.2f}")
print("Desconto de".upper(), f"{porcentagem}%")
    
    
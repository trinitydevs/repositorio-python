def valorPagamento(valorPrestacao, diasAtraso):
    if (diasAtraso <= 0):
        return valorPrestacao
    else:
        multa = valorPrestacao * 0.03
        juros = valorPrestacao * (0.001 * diasAtraso)
        valorTotal = valorPrestacao + multa + juros
        return valorTotal

totalPrestacoes = 0
totalValorPago = 0

while True:
    valorPrestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))
    if (valorPrestacao == 0):
        break
    diasAtraso = int(input("Digite o número de dias em atraso: "))
    
   

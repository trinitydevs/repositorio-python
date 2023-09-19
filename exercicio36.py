nLados = int(input("Informe o n° de lados de um polígono regular: "))
medida = float(input("Informe a medida: "))

if(nLados == 3):
    print("Triângulo!")
    print("Perímetro: ", medida*nLados)
elif(nLados == 4):
    print("Quadrado!")
    print("Área: ", medida**2)
elif(nLados == 5):
    print("Pentágono!")
elif(nLados < 3):
    print("Não é polígono!")
else:
    print("Polígono não identificado")

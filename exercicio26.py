altura = float(input("Informe a sua altura: "))
genero = str(input("Informe o gênero: M ou F "))

pesoIdealM = (72.7 * altura) - 58
pesoIdealF = (62.1 * altura) - 44.7

if(genero == "M" or genero == "m"):
    print("Peso ideal: ", pesoIdealM,"kg")
elif(genero == "F" or genero == "f"):
    print("Peso ideal: ", pesoIdealF,"kg")
else:
    print("Nos informe o gênero!")

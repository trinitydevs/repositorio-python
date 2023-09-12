idade = int(input("Informe a sua idade: "))

if(idade > 1 and <= 13):
    print("Você é uma criança!")
elif(idade > 13 and <= 20):
    print("Você é um adolescente!")
elif(idade > 20 and <= 50):
    print("Você é um adulto!")
else:
    print("Vooê é um idoso!")
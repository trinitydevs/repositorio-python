contagem = 0
contador = 5

temp = float(0)
for contagem in [1, 2, 3, 4, 5]:
    temperatura = float(input("Informe a temperatura do cliente: "))
    temp += temperatura
    if(temperatura <= 37.2):
        print(temperatura,"°C: temperatura normal!")
    elif(temperatura >= 37.3 and temperatura <= 38):
        print(temperatura,"°C: estado febril!")
    elif(temperatura == 39):
        print(temperatura,"°C: febre!")
    else:
        print(temperatura,"°C: febre alta!")
        
        
print("Quantidade de pessoas analisadas:", contagem)
print("Média de temperatura: ", float(temp/5),"°C")


   
    
dia = int(input("Digite o dia tipo data: "))
mes = int(input("Digite o mês tipo data: "))
ano = int(input("Digite o ano: "))

if(mes == 1 and dia >=1 and dia <=31):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 2 and dia >=1 and dia <=29 and ano%400 == 0 or ano%4 == 0 and ano%100 != 0):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 3 and dia >= 1 and dia <=31):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 4 and dia >=1 and dia <=30):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 5 and dia >=1 and dia <=31):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 6 and dia >=1 and dia <=30):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 7 and dia >=1 and dia <=31):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 8 and dia >=1 and dia <=31):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 9 and dia >=1 and dia <=30):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 10 and dia >=1 and dia <=31):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 11 and dia >=1 and dia <=30):
    print(f'{dia}/{mes}/{ano} é válido!')
elif(mes == 10 and dia >=1 and dia <=30):
    print(f'{dia}/{mes}/{ano} é válido!')
else:
    print(f'{dia}/{mes}/{ano} NÃO é uma data válida!')









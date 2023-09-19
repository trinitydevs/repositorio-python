num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1/num2

resposta = str(input("Deseja calcular as quatro operações? Digite sim ou não "))
if(resposta == "Sim" or resposta == "sim" or resposta == "SIM" or resposta == "S"):
    print("ADIÇÃO:", num1,"+",num2 ,"=", adicao)
    print("SUBTRAÇÃO:", num1,"-",num2 ,"=", subtracao)
    print("MULTIPLICAÇÃO:", num1,"x",num2 ,"=", multiplicacao)
    print("DIVISÃO:", num1,"÷",num2 ,"=", divisao)
else:
    print("Certo.")


print("CAMPEONATO DE NATAÇÃO")
idade = int(input("Informe a sua idade: "))

if(idade >= 5 and idade <= 7):
    print("Você foi selecionado para a categoria 'infantil A'")
elif(idade >= 8 and idade <= 11):
    print("Você foi selecionado para a categoria 'infantil B'")
elif(idade == 12 or idade == 13):
    print("Você foi selecionado para a categoria 'Juvenil A'")
elif(idade >=14 and idade <= 17):
    print("Você foi selecionado para a categoria 'Juvenil B'")
elif(idade >=18):
    print("Você foi selecionado para a categoria 'Adulto'")
else:
    print("Você ainda não atingiu a idade requerida para participar do campeonato!")







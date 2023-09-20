for contagem in range (0, 1):
    nome = str(input(("Digite o seu nome: ")))
    print(nome)
    senha = input("Digite uma senha: ")
    print(senha)
    if(senha == nome):
        print("Erro! Usuário e senha não podem ser iguais!")
        nome = str(input(("Digite o seu nome: ")))
        print(nome)
        senha = input("Digite uma senha: ")
        print(senha)

        
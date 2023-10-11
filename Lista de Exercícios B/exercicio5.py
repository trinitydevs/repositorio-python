atletas = []
while True:
    nome = input("Digite o nome do atleta (Enter para encerrar o programa): ")
    if(nome == ""):
        break
    atleta = {"nome": nome,"saltos": [],"media": 0,}
    for i in range(5):
        atleta.get("saltos").append(
            float(input(f"Distância do {i+1}º salto: "))
        )
    atleta.get("saltos").sort()
    atleta["media"] = sum(atleta.get("saltos"))/ 3
    print(f"\nMédia dos saltos: {atleta.get('media'):.1f} m\n")
    atletas.append(atleta)

print("\n\nResultado final:")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f}m")
    print(f"{atleta.get('nome')}: {atleta.get('saltos')}")

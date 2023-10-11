
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

temperaturas = []
for i in range(12):
    temperaturas.append(float(input(f"Digite a temperatura de {meses[i]} em °C: ")))
    
media = sum(temperaturas)/12
print(f"\nA média das temperaturas foi {media:.2f}°C")
print("Meses com temperaturas acima da média: ")
for i in range(12):
    if (temperaturas[i] > media):
        print(f"{i+1} - {meses[i].capitalize()} com {temperaturas[i]:.2f}°C")


carros = ['Renegade', 'Opala 67', 'Vectra', 'Hilux', 'Brasilia 74']
consumo = [5, 2, 12, 9, 2] #km
valorLitro = 2.25 #valor
distancia = 1000 #km

print("VEÍCULO  -  MODELO -    CONSUMO ")
for i in range(len(carros)):
    print(f"Veículo {i+1}: {carros[i]} -  1L - {consumo[i]}km")
print(" ")
print(f"Modelo mais econômico: {carros[2]} - {max(consumo)}km por litro")
print("")
for y in range(len(carros)):
    print(f"{carros[y]} - R${(distancia*valorLitro)/consumo[y]} --> 1000km - {distancia/consumo[y]:.0f}l" )
lista1 = (2, 4, 5, 5)
lista2 = (3, 3, 9, 10)
listaConcat = list(lista1 + lista2)
print(listaConcat)
print("Ordem crescente:", sorted(listaConcat, key=int))
print("Ordem decrescente:", sorted(listaConcat, key=int, reverse=True))


#           0       1         2
lista = ["Bruno", "Denis", "Rafa", "Glória", "Beatriz","Flávio","João"]

nome = lista[1]
print(nome)

print(lista[0])
print(lista[-1])
print(lista[2:5])
print(lista[:4])
print(lista[3:])
print(lista[-4:-1])

if "Rafa" in lista:
    print("Sim, Rafa está na lista.")
else:
    print("Não, Rafa não está na lista.")
    
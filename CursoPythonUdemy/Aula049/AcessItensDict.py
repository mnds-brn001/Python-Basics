dict1 = {
    "Nome": "Bruno",
    "Sobrenome": "Mendes",
    "Ano": 2001
}

#x = dict1["Sobrenome"]
#print(x)
print(dict1["Sobrenome"])

# x = dict1.get("Nome")
print(dict1.get("Nome"))

x = dict1.keys() # Exibe as chaves da coleção.
print(x)

dict1["Idade"] = 21
print(x)

x = dict1.values() # Exibe os valores da coleção.
print(x)
dict1["Altura"] = 1.75
print(x)

# Os itens da coleção de dicionários são separados por Tuplas que por sua vez são uma combinação de chaves:valor.
x = dict1.items()
print(x)

dict1["Altura"] = 1.76
print(x)

if "Idade" in dict1:
    print("Sim, Idade está em dict1")
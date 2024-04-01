# Dicionários são coleções de itens e sao armazenados de forma ordenada.
# São ordenados, alteráveis e não permitem itens duplicados.

# São representados pela Sintaxe: {'chave':'valor'}

dict1 = {
    "Nome":"Bruno",
    "Sobrenome": "Mendes",
    "Idade": 21,"Altura": 175,
    "Amigos":["Denis","João"],
    123:False
    }

 # A indexação é feita utilizando o "nome" da >>chave<<
print(dict1)
print(dict1["Nome"])
print(dict1["Sobrenome"])
print(dict1["Idade"])
print(dict1["Altura"])
print(dict1["Amigos"])
print(len(dict1))
print(type(dict1))
lista = [2, 4,5,6,7,8,9,0,11,13]

nova_lista = filter(lambda item: item % 2 != 0, lista)
print(list(nova_lista))
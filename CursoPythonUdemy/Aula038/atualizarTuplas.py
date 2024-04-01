x = ("Bruno","Denis","Arthur")
print(x)

y = list(x) #Alterando a tupla pelo método de atribuiçao a uma variável e logo depois trocando o item usando a indexação na variável.
y[1] = "Iago"
x = tuple(y) # Depois reverte-se a variável para uma tupla.
print(x)

# y = list(x) # Processo semelhante ao outro, porém aqui está adicionando um item à tupla.
# y.append("Lucas") # Transforma em lista, depois utiliza o método .append() e então retorna à tupla.
# x = tuple(y)

y = ("Lucas",) # Somando tuplas.
x += y
print(x)

y = list(x)
y.remove("Arthur")
x = tuple(y)
print(x)


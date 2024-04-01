# É uma coleção ordenada e imutável. São escritas entre parenteses.

tupla = ("Bruno","Denis","Arthur")

print(tupla)
print(len(tupla))

tupla2 = ("Carro",) #<class 'tuple'>
print(type(tupla2))

tupla3 = ("Carro") # <class 'str'>
print(type(tupla3))

tupla4 = (1,5,4,25)
tupla5 = (False,True, True)
tupla6 = ("Bruno",21,126.114,True)

tupla7 = tuple(("Maça", 2022, "Banana.37", False))
print(tupla7)
print(type(tupla7))
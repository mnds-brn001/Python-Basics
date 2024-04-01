x = ["apple", "banana"]
y = ["apple", "banana"] #X e Y obtem o mesmo TIPO e CONTEÚDO.
z = x

print(x is z) #Operador de identidade
print(x is y) #Operador de identidade
print(x == y)

print(x is not z) #Operador de identidade
print(x is not y) #Operador de identidade
print(x != y)

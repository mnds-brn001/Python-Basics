x = lambda a : a + 10
#result = x(5)
print(x(5))

x = lambda a, b : a * b
print(x(2,5))

def myFunction(n):
    return lambda a : a * n

meuDuplicador = myFunction(2)
print(meuDuplicador(11))

meuTriplicador = myFunction(3)

print(meuTriplicador(11))
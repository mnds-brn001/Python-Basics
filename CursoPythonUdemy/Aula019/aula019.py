print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 330

if b > a:
    print("Sim, b é maior do que a.")
else:
    print("Não, b não é maior do que a.")

print(bool("Ola"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))
x = 0
y = ""
print(bool(x))
print(bool(y))

# Valores que retornam falso

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


def myFunction():
    return True

print(myFunction())

if myFunction():
    print("Sim!")
else:
    print("Não!")

x = 200
print(isinstance(x, int)) #(isinstance(variavel,tipo a ser conferido)Confere o tipo da variável e retorna uma expressão booleana(True or False).


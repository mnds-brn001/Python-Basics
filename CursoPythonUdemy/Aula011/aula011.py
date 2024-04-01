import random

# Classe de inteiros
a = 1
b = 128361836186812
c = -123432

print(type(a))
print(type(b))
print(type(c))


#Classe de reais (float)
d = 1.10
e = 1.0
f = -35.59
g = 35e3 #Notação científica.
h = 12E4
i = -75.7e100

print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

# Classe dos complexos(j).
j = 3+5j
k = 5j
l = -5j

print(type(j))
print(type(k))
print(type(l))


# Converter de INT para FLOAT:
x = float(1)

#Converter de FLOAT para INT:
y = int(2.8)

#Converter de INT para COMPLEX:
z = complex(x)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

num = random.randrange(1,10)

print(num)
print(random.randrange(1,10))
print("\n")
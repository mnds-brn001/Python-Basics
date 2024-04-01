#Utiliza-se indexação para acessar aos itens da tupla, semelhante às listas
# Igualmente às listas também é possível utilizar a indexação negativa.
#(0,1,2,3,..) (...,-3,-2,-1)
tupla1 = ("Bruno","Denis","Arthur","Beatriz","João","Lucas")
print(tupla1)
print(tupla1[0])
print(tupla1[-1])
print(tupla1[2:5])
print(tupla1[:4])
print(tupla1[2:])
print(tupla1[-4:-1])
print(tupla1[:-4])

print("Denis" in tupla1) # Devolve no print um valor booleano. (item in x).

if "Denis" in tupla1:
    print("Sim, está presente na tupla.")
else:
    print("Não está presente.")


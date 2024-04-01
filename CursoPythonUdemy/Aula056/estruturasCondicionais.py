#igual a: a == b
#Diferente de: a != b 
#Menor que: a < b
#Menor ou igual a: a <=b 
#Maior que: a > b
#maior ou igual a: a >=b

a = 150
b = 200

if b < a:
    print("b é maior do que a")
    print("Segunda  instrução")
elif a == b: #O bloco elif só é executada se for uma expressão verdadeira e anterior for falsa.
    print("a é igual a b")
elif a + 50 !=b:
    print("a é diferente de b")
else:
    print("Todas as verificações foram falsas.")
#if b < a:
#    print("b é maior do que a")
#    print("Segunda  instrução")

print("Fim do Programa.")
x = "incrível" # variável global

def myFunc():
    global x
    x = "inacreditável"
    y = "fantástico" #VARIAVEL LOCAL
    global z
    z = "Bem vindo ao curso"
    print("Python é " + x + " e " + y) # } varíavel local
    print(z)
#A função dá preferência a variáveis locais.

myFunc()

print("=====================")
print("Você é " + x)
print(z)


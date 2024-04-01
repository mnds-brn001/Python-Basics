idade = 21
txt = "Eu sou o Bruno e tenho {} anos de idade" 
print(txt.format(idade))

quantidade = 3
item = "bolo"
valor = 14.99
meuPedido = "Eu quero {} pedaços de {} por {} reais."
meuPedido2 = "Eu quero pagar {2} reais pelos {0} pedaços de {1}"

print(meuPedido.format(quantidade,item,valor))
print(meuPedido2.format(quantidade,item,valor))

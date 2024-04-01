nomes = ("Bruno","Denis","Arthur","Lucas","João")
print(nomes)

# (nome1, nome2, nome3) = nomes
#(nome1, nome2, *nome3) = nomes
(nome1, *nome2, nome3) = nomes
print(nome1)
print(nome2)
print(nome3)

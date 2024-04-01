def nomeCompleto(nome, sobrenome):
    print(nome + " " + sobrenome)

def listaNomes(*nomes):
    for x in nomes:
        print(x)

nomeCompleto("Bruno", "Mendes")
listaNomes("Bruno","Denis","Arthur")

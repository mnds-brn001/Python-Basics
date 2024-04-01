def nomes(primeiro, segundo, terceiro):
    print("O Primeiro nome é", primeiro)
    print("O Segundo nome é", segundo)
    print("O Terceiro nome é", terceiro)

nomes(segundo = "Bruno", terceiro ="Denis", primeiro = "Arthur")

def nomeCompleto(**nome):
    print(nome)
    for x in nome.values():
        print(x)


nomeCompleto(pri = "Bruno", seg = "Purificacao", ter = "Mendes")
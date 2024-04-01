class Pessoa:
    def __init__(meuObjeto, nome, idade) -> None:
        meuObjeto.nome = nome
        meuObjeto.idade = idade

    def myFunc(self):
        print("Ola meu nome é " + self.nome)

p1 = Pessoa("Dani", 21)
p1.myFunc()
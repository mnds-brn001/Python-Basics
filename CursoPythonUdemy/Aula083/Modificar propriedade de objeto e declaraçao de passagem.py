#class Pessoa:
#    pass

#p1 = Pessoa()

class Pessoa:
    def ___init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def myFunc(self):
        print("Ola meu nome é " + self.nome)

p1 = Pessoa("Bruno", 21)
p1.myFunc()

p1.nome = "Dani"
p1.myFunc()
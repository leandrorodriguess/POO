# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
# Decorator  @classmethod
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)

p2 = Pessoa.criar_com_50_anos('Helena')

p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p1.nome, p1.idade) # Criada pelo Construtor
print(p2.nome, p2.idade) # Criado pelo decorator (fabrica de metodo >> criar_com_50_anos
print(p3.nome, p3.idade) # Criado pelo decorator (fabrica de metodo >> criar_com_50_anos
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

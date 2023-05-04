# @staticmethod (métodos estáticos)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.
# Decorator @staticmethod

class Classe:

    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)

def funcao(*args, **kwargs):
    print('Oi', args, kwargs)


c1 = Classe()

# metodo statico (possui acesso) exclusivamente dentro do metodo
c1.funcao_que_esta_na_classe(1, 2, 3, 4, 5, 6, 7, 8, 9, "Leandro", bool, 1.2)

# não pertence a classe e realiza a mesma operação
funcao(1, 2, 3)

#parametros nomeado dinamicamente
Classe.funcao_que_esta_na_classe(nome="leandro", idade= 13, outro_parametro = "other")
funcao(nomeado=1)

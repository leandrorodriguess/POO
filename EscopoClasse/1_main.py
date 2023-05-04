from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

# instacia da classe
p3 = Pessoa("Leandro Souza", 20)
p3.falar("Aula de POO passo a passo")
p3.comer("Maça")
p3.falar("Vamos Embora Meu Povo")
p3.parar_comer()
p3.comer("Banana")
p3.comer("Maça")
if ((p3.GetAnoNascimento()) < 2002):
    print("seria uma validação baseada no retorno do método")
else:
    print("É parceiro, você não passou no teste")

# comentário de uma linha

""" comentário demonstrando que o ID dos objetos são diferentes
    Por serem instancias diferentes
"""
# print(p2)
# print(p1)


# print(p1.get_ano_nascimento())
# print(p2.get_ano_nascimento())

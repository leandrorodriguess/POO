"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
print(lista[-4])
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
print(lista[1], type(lista[1]))


"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
print(lista)
lista[2] = 'Leandro'
print(lista)
del lista[1]
print(lista)
print(lista[2])
lista.append(50)
print(lista)
lista.pop()
print(lista)
lista.append(60)
print(lista)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

lista.insert(0, 5)
print(lista)
# insere no final não existindo o indice
lista.insert(110, 5)
print(lista)
lista.clear()

lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 7, 8]

lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)


"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()


lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

lista_a = lista_b
print(lista_a)
print(lista_b)
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))


lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
print(lista)


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

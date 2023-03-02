"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'

# até o final
print(variavel, ' >> variavel[4:]', variavel[4:])

# do início até uma quantidade
print(variavel, ' >>  variavel[:3]', variavel[:3])


# fatiamento até o indice 5
print(variavel, ' >> variavel[2:6]', variavel[2:6])

# fatiamento até
print(variavel, ' >> variavel[0:5]', variavel[0:5])

# tamanho de uma variavel
print(len(variavel))

# impressão com passo de dois em dois
print(variavel[0:5:2])

# impressão com passo de dois em dois
print(variavel[0:5:-1])

# Impressão de toda string invertida
variavel = "socorram-me subi no onibus em marrocos"
print(variavel[::-1])

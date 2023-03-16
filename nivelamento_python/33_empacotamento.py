"""
Introdução ao empacotamento e desempacotamento
"""
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

nome, variavel2, *resto = ['Maria', 'Helena', 'Luiz', 'Leandro']
print(resto)
print(variavel2)
print(resto)
print(type(variavel2))
print(type(resto))

nome, variavel2, *resto = ['Maria', 'Helena']
print(resto, '>>', type(resto))

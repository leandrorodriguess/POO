"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
# string[3] = 'ABC'

# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)

# preenche restante com zeros
print(string.zfill(10))

string = 'leandro rodrigues da silva souza'
print(string.capitalize())

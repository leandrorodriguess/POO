# Tipagem forte, não converte um tipo em outro baseado na operação.
# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print((float('1') + 1))
print(bool(1))

# polimorfismo
print(str(11) + 'b')

print(11 + 'b')

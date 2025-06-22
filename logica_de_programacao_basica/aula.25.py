"""
Interpolação básica de strings
s -> string
d e i -> int
d -> float
x e X -> Hexadecimal1 (ABCDEF0123456789)
"""
nome = 'Bruno'
preco = 1000.95897643
variavel = '%s, o preço é %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (15, 15))

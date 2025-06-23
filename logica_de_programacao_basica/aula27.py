"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] -> início__fim__passo 
[::] -> pega a string inteira 
Obs.: a função len retorna a qtd
de caracteres da str 
"""
variavel = 'Olá mundo'
print('##########')
print(variavel[5])
print(variavel[-4])
print('##########')
print(variavel[4:])
print(variavel[4:7])
print(variavel[4:8])
print('##########')
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print('##########')
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print('##########')
print('Inverte a string')
print(variavel[-1:-10:-1])
print(variavel[::-1])
print('##########')

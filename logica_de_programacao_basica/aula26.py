"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes do zeros
Sinal + ou -
Ex.: 0>-100,.1f
Convertion flags - !r !s !a
"""

variavel1 = 'ABC'
print(f'.{variavel1}.')
print(f'.{variavel1: >10}.')
print(f'.{variavel1: <10}.')
print(f'.{variavel1: ^10}.')
print('*******************')
print(f'.{variavel1:0>10}.')
print(f'.{variavel1:0<10}.')
print(f'.{variavel1:0^10}.')
print('*******************')
print(f'.{variavel1:$>10}.')
print(f'.{variavel1:$<10}.')
print(f'.{variavel1:$^10}.')
print('*******************')
print(f'.{variavel1:_>10}.')
print(f'.{variavel1:_<10}.')
print(f'.{variavel1:_^10}.')
print('*******************')
print(f'.{variavel1:*>10}.')
print(f'.{variavel1:*<10}.')
print(f'.{variavel1:*^10}.')
print('*******************')
print(f'{1000.4123:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08X}')
print(f'{variavel1!r}')

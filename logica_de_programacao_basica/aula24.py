# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# B r u n o
# -6 -5 -4 -3 -2 -1
nome = 'Bruno'
# print(nome[2])
# print(nome[-3])
print('B' in nome)
print('z' in nome)
print('uno' in nome)
print('avio' in nome)
print('uno' not in nome)
print('avio' not in nome)
print('_______________________')
print('_______________________')
# exercício
palavra = input('Digite uma palavra: ')
encontrar = input('Digite a letra para verificação: ')
if encontrar in palavra:
    print(f'A letra {encontrar} contém na palavra {palavra}.')
else:
    print(f'A letra {encontrar} não consta na palavra {palavra}.')

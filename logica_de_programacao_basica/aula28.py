"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
----- Exiba:
--------- Seu nome é {nome} - feito
--------- Seu nome invertido é {nome_invertido} - feito
--------- Se nome contem ou não espaços
--------- Seu nome tem {n} letras
--------- A primeira letra do seu nome é {letra} - feito
--------- A última letra do seu nome é {letra} - feito
--------- Se nada for digitado em nome ou idade:
------ Exiba:
--------- "Desculpe, você deixou campos vazios
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]
primeira_letra = nome[0]
ultima_letra = nome[nome[-1]]
mensagem = ''
letras = len(nome)

if ' ' in nome:
    mensagem = 'Seu nome contém espaços'
else:
    mensagem = 'Seu nome não contém espaços'

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    print(mensagem)
    print(f'Seu nome tem {letras} letras')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A última letra do seu nome é {ultima_letra}')
else:
    print('Desculpe, você deixou campos vazios')

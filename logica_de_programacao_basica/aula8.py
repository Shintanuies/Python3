nome = 'Bruno'
sobrenome = 'Vidal'
idade = 38
ano_atual = 2025
ano_de_nascimento = ano_atual - idade
maior_de_idade = idade >= 18
altura_em_metros = 1.72

if maior_de_idade:
    maior_de_idade = 'sim'
else:
    maior_de_idade = 'não'

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_de_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros', altura_em_metros)

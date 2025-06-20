# INTRODUÇÃO A VARIÁVEIS EM PYTHON

# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# búmeros e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = espressão
nome_completo = 'Bruno Gomes da Rosa Vidal'
soma_dois_mais_dois = 2 + 2
print(nome_completo, soma_dois_mais_dois)

int_um = int('1')
print(int_um, type(int_um))

int_um = bool('1')
print(int_um, type(int_um))

nome = 'Bruno'
idade = 38
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior de idade?:', maior_de_idade)

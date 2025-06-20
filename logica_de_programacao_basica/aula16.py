# Introdução aos blocos de código + if / elif / else (condicionais)

# if / elif      / else
# se / se-não-se / se-não

entrada = input('Você quer "entrar" ou "sair" do sistema? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Digite uma opção valida por favor')

print('FORA DO BLOCO CONDICIONAL')  # Sempre será executado

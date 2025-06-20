# Exercício de programação com if e comparação

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor_tipo = type(primeiro_valor)
print(f'Tipo valor 1: {primeiro_valor_tipo}')

segundo_valor_tipo = type(segundo_valor)
print(f'Tipo valor 2: {segundo_valor_tipo}')

primeiro_valor_int = int(primeiro_valor)
print(f'Tipo convertido valor 1: {type(primeiro_valor_int)}')

segundo_valor_int = int(segundo_valor)
print(f'Tipo convertido valor 1: {type(segundo_valor_int)}')

if primeiro_valor_int > segundo_valor_int:
    mensagem = 'é maior do que'
elif primeiro_valor_int < segundo_valor_int:
    mensagem = 'é menor que'
else:
    mensagem = 'é igual a'

print(
    f'primeiro_valor = {primeiro_valor_int} {mensagem} segundo_valor = {segundo_valor_int}')

print(f'{primeiro_valor_int} {mensagem} {segundo_valor_int}')

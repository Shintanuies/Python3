# Usando a função input para coletar dados do usuário

# nome = input('Qual o seu nome?\n')
# print(f'O seu nome é {nome}')

numero_um = input(f'Digite um número: ')  # Recebe uma str
numero_dois = input(f'Digite outro número: ')  # Recebe uma str
# Usando int para converter de str para int, se não fizermos isso ocorrerá um erro
soma = int(numero_um) + int(numero_dois)
print(f'A soma dos números é: {soma}')

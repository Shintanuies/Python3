#  Operador Lógico "or"

# Operadores lógicos
# and (e) or (ou) not (não)
# and -> Todas as condições presiisam ser
# verdadeiras.
# Se qualquer valor for consideradofalso,
# a expressão inteira será avaliada naquele valor
# falso.
# São considerados falsy (que vc já viu)
# # 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or 'e') and (senha_digitada == senha_permitida):
    print('Entrar')

else:
    print('Sair')

print('____________________')

# Avaliação de curto circuito
# Retorna o primeiro valor verdadeiro
print(True or False or 0)
print(0 or False or 'abc')
print(0 or False or 'abc' or True)
print(0 or False or True or 'abc')

print('____________________')

senha = input('Senha: ') or 'sem senha'
print(senha)

#  Operador Lógico "and"

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

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')

print('____________________')

# Avaliação de curto circuito
# Retorna aquele False da expressão sem continuar # checando o resto da expressão.
print(True and False and True)
print(True and 0 and True)

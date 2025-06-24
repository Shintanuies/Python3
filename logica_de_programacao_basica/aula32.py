"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
# ========================================================
# ---INÍCIO
numero_inteiro_str = input('Digite um número inteiro: ')
mensagem_par = 'par'
mensagem_impar = 'impar'

try:
    numero_inteiro_int = int(numero_inteiro_str)
    if numero_inteiro_int % 2 == 0:
        print(f'O numero {numero_inteiro_int} é {mensagem_par}')
    else:
        print(f'O numero {numero_inteiro_int} é {mensagem_impar}')

except:
    print('Vocè NÃO digitou um número inteiro')
# ---FIM
# ===================================================
"""
Faça u programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa note 12-23.
"""
# ===================================================
# ---INÍCIO
hora_str = input('Digite uma hora inteira: ')

try:
    hora_int = int(hora_str)
    if hora_int > 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int > 11 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int > 17 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida')
except:
    print('Você não digitou uma hora inteira')
# ---FIM
# ====================================================
"""
#=====================================================
Faça um programa que peça primeiro o nome do usuáriuo, Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
# ---INÍCIO
nome_usuario = input('Digite seu nome: ')
tamanho_nome_usuario = len(nome_usuario)
if tamanho_nome_usuario <= 4:
    print('Seu nome é curto!')
elif tamanho_nome_usuario > 4 and tamanho_nome_usuario <= 6:
    print('Seu nome é normal')
else:
    print('Seu nomeé muito grande!')
# ---FIM
# =====================================================

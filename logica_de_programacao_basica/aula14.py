# Formatação de strings com o método format

a = 'A'
b = 'B'
c = 1.1
string = 'b={} A={} C={}'
formato = string.format(a, b, c)

string_dois = 'b={1} a={0} c={2}'  # Usando o Índice
formato_dois = string_dois.format(a, b, c)  # Argumentos

string_tres = 'a={} b={} c={:.2f}'
formato_tres = string_tres.format(a, b, c)  # Argumentos

string_quatro = 'a={nome1} b={nome2} c={nome3:.2f}'
formato_quatro = string_quatro.format(nome1=a, nome2=b, nome3=c)  # Parâmetros

print(formato)
print(formato_dois)
print(formato_tres)
print(formato_quatro)

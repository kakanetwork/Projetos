
# Programa que Informa se o valor informado pertence aos Números Triangulares
''' Definição: Números Triangulares são aqueles números que quando colocados em certa ordem, conseguem
formar um Triângulo!
Exemplo: 3 = .:.
'''

num = int(input('Informe um Número: '))
var = 0
cont = 1
cont2 = 0
while var <= num:
    var += cont 
    cont += 1
    if var == num:
        print(f'O Número {num}, é um Número Triangular!')
        cont2 += 1
if cont2 == 0:
    print(f'O Número {num}, não é um Número Triangular!')
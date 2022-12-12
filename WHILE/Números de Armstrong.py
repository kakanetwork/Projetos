
# Programa que Informa se o Número pertence ou não aos Números de Armstrong

''' Definição: Os Números de ARMSTRONG, são aqueles cujo cada digito elevado a 
quantidade total de digitos e somados ao final, tem como resultado o Próprio Número Base
Exemplo: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
'''

num = int(input('Informe um Número Positivo: '))
num = abs(num)
aux = num
soma = 0
cont = 1
tamanho = 0

while cont <= aux: # Estrutura de Repetição para a coleta da Quantidade de Digitos que possui o Valor informado
    cont *= 10
    tamanho += 1 # Coletagem de quantidade de Digitos

while num > 0: # Estrutura de Repetição Principal - Fragmentação e Potência dos digitos
    digito = num%10 # Parte 1 - Utilizado para a Fragmentação do Número, exemplo: 153 = 1,  5,  3
    potencia = digito**tamanho # Parte 2 - Elevando o Digito Fragmentado a Potência, onde Potência = total de Digitos
    soma = potencia + soma # Parte 3 -  Soma de todos os Digitos elevados, que formara a Condição para ser ou Não o Número de Armstrong
    num = num // 10 # Parte 1 - Utilizado para complementação da Fragmentação

if soma == aux: # Condição onde a soma da Parte 3 for igual ao valor inicial informado, ele será um Número de Armstrong
    print(f'O número {aux}, pertence aos Números de ARMSTRONG!')
else:
    print('O número {aux}, não pertence aos Números de ARMSTRONG!')

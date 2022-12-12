num = int(input('Informe um Número Positivo: '))
num = abs(num)
aux = num
soma = 0
cont = 1
tamanho = 0
while cont <= aux:
    cont *= 10
    tamanho += 1
while num > 0:
    digito = num%10
    potencia = digito**tamanho
    soma = potencia + soma
    num = num // 10
if soma == aux:
    print(f'O número {aux}, pertence aos Números de ARMSTRONG!')
else:
    print('O número {aux}, não pertence aos Números de ARMSTRONG!')

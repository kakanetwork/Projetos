valor = int(input('Informe um valor positivo: '))
valor = abs(valor)
if valor != 0:
    divisor = 1
    contdiv = 0
    while divisor <= valor:
        if valor % divisor == 0:
            print(f'Os divisores são {divisor}')
            contdiv += 1
        divisor += 1
    if contdiv == 2: print('E o Número é primo!')
    else: print('E o Número não é Primo!')
else: print('Informe um Valor diferente de Zero!')


dec = int(input('Informe o Número em Decimal para a Conversão: '))
dec = abs(dec)
binario = ''
for x in range(dec+1):
    if dec > 0:
        resto = dec%2 
        dec = dec//2
        binario = str(resto)+binario 
print(f'\nSeu Número em Binário é correspondente a: {binario}')
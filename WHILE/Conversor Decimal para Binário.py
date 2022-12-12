
# Programa para Conversão de qualquer número decimal para Binário

dec = int(input('Informe o Número em Decimal para a Conversão: '))
dec = abs(dec)
binario = '' # Utilizando String Vazia, para armazenamento dos Binários

while dec > 0:
    resto = dec%2 # Calculo do resto quando dividido por 2, sendo o resto o número binário
    dec = dec//2

    binario = str(resto)+binario # Concatenação do resto transformado em string, sendo adicionado na String Vazia
print(f'\nSeu Número em Binário é correspondente a: {binario}')

# Programa Informa o Fatorial do valor informado

valor = int(input('Insira um valor inteiro:'))
aux = valor
var = 1
fat = valor

if valor !=0: # Condição onde o Valor deve ser diferente de Zero

    while valor > 1: # Estrutura de Repetição onde vai se realizar o Calculo Principal
        valor -= 1
        var = aux*valor
        aux = var
    print (f'{fat}!= ',var) # Informando o Usuário do Fatorial daquele Número
    
else:
    print('0! = 1')
valor = int(input('Insira um valor inteiro:'))
aux = valor
var = 1
fat = valor
if valor !=0:
    while valor > 1:
        valor -= 1
        var = aux*valor
        aux = var
    print (f'{fat}!= ',var)
else:
    print('0! = 1')
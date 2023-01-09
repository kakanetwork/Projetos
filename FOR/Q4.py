valor = int(input('Informe um valor inteiro para verificar seu fatorial: '))
aux = valor
var = 1
fat = valor
if valor !=0:
    for x in range(1,valor):
        valor -= 1
        var = aux*valor
        aux = var
    print (f'{fat}!= ',var)
else:
    print('O Número informado foi ZERO, portanto, fatorial é = 1')
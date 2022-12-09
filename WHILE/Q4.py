Num = 1000
print('\nOs números de 1000 - 2000 que possuem resto igual a 5 quando divididos por 11 são: \n')
while Num <= 2000:
    if Num%11 == 5: print(Num, end=' - ')
    Num += 1
print('FIM!')
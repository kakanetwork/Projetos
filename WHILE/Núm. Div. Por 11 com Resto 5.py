
# Programa que informa os números entre 1000 e 2000 que possuem resto igual a 5 quando divididos por 11

Num = 1000
print('\nOs números de 1000 - 2000 que possuem resto igual a 5 quando divididos por 11 são: \n')

while Num <= 2000: 
    if Num%11 == 5: print(Num, end=' - ') # Calculo e Print dos numeros correspondentes a questão
    Num += 1
print('FIM!')
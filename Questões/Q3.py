
'''if valor != 0:
    cont = 1
    primo = 0
    while cont <= valor:
        if valor%cont == 0:
         cont += '''
#valor = 10
#divisor = 1
#numprimo = 1
#cont = 0
#while numprimo <= valor:
  #  if numprimo % divisor == 0:
      #  numprimo += 1
      #  cont += 1
    #divisor += 1
#if cont == 2:
       # print(cont)
#valor = 10
#if valor != 0:
   # divisor = 1
   # contdiv = 0
   # valor2 = 1
  #  while divisor <= valor:
     #   if valor2 % divisor == 0:
       #     contdiv += 1
      #  divisor += 1
 #   if contdiv == 2:
    #    print('E o Número é primo!')


    #if valor1 % numprimo != 0:
        #print(numprimo)
        #numprimo += 1
       # valor1 += 1
    
    
#dec = 10
#valor1 = 1
#valor2 = 1
#primos = ''
#while dec >= valor2:
    #if valor1 % valor2 == 0:
        #valor1 += 1
        #valor2 += 1
    #elif valor1 % valor2 != 0: 
        #valor3 = valor1 // valor2
        #primos = str(valor3)+primos
#print(primos) 

'''valor = 10
valor = abs(valor)
if valor !=0:
    cnt = 0
    valor_1 = 1
    while valor_1 <= valor:
        divisor = 1
        while divisor <= valor_1:'''



valor = int(input('Informe um valor positivo: '))
valor = abs(valor)
if valor != 0:
    divisor = 1
    contdiv = 0
    while divisor <= valor:
        if valor % divisor == 0:
            contdiv += 1
        divisor += 1
    if contdiv == 2: print(f'Os divisores são {divisor}')
    else: print('E o Número não é Primo!')
else: print('Informe um Valor diferente de Zero!')


palavra = input('Informe uma palavra: ')
var1 = palavra.upper()
cont = ''
for palindromo in range(len(var1)-1, -1, -1):
    cont += var1[palindromo]
if cont == var1:
    print(f'{palavra} é um palíndromo')    
else:
    print(f'{palavra} não é um palíndromo')
var1 = int(input('Informe o Primeiro número: '))
var2 = int(input('Informe o Segundo número: '))
if var1 > var2:
    maior = var1
    menor = var2 
else:
    maior = var2
    menor = var1
for cont in range(100):
    var3 = maior % menor
    if var3 == 0:
        break
    maior = menor
    menor = var3
print(f'O MDC (Máximo Divisor Comum) de {var1} e {var2} é {menor}\n')
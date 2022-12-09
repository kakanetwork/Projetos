
# Entrada de Dadis
a1 = float(input('Informe o primeiro ângulo: '))
a2 = float(input('Informe o segundo ângulo: '))
a3 = float(input('Informe o terceiro ângulo: '))

# Condição das Propriedades dos tipos de Triângulos e onde todos os Ângulos devem ser positivos
if a1 > 0 and a2 > 0 and a3 > 0 and a1 + a2 < a3 and a1 + a2 < a3 and a1 + a2 < a3:

    # Condição onde Destina o Resultado a cada tipo de Triângulo
    if a1 == a2 and a1 == a3:
        print('É um triângulo equilatero!')
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
else:
    print('Não condiz com um Triângulo!')
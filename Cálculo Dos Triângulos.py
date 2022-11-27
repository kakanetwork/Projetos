# Entrada de Dados
a1 = float(input('Informe o primeiro ângulo: '))
a2 = float(input('Informe o segundo ângulo: '))
a3 = float(input('Informe o terceiro ângulo: '))

# Soma dos ângulos internos onde obrigatoriamente devem ser iguais a 180°
soma = a1 + a2 + a3

# Condição onde se mede que todos devem ser Números Positivos e a Soma seja 180°, para que haja Triângulo
if a1 < 0 or a2 < 0 or a3 < 0 or soma != 180:
    print('\nA Soma dos ângulos internos deve ser de 180°, e todos os Ângulos devem ser Positivos!')
elif a1 == 90 or a2 == 90 or a3 == 90:
    print('\nAs medidas informadas correspondem a um Triângulo Retângulo!')
elif a1 < 90 and a2 < 90 and a3 < 90:
    print('\nAs medidas informadas correspondem a um Triângulo Acutângulo!')
else:
    print('\nAs medidas informadas correspondem a um Triângulo Obtusângulo!')
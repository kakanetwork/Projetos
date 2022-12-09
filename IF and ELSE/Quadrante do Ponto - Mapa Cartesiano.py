
# Entrada de Dados
x = float(input("Informe o Valor de X: "))
y = float(input("Informe o Valor de Y: "))

# Condições para que se descubra a qual quadrante pertence o valor
if x > 0 and y > 0:
    print('\nSe encontra no 1° Quadrante!')
elif x > 0 and y < 0:
    print('\nSe encontra no 2° Quadrante!')
elif x < 0 and y < 0:
    print('\nSe encontra no 3° Quadrante!')
else:
    print('\nSe encontra no 4° Quadrante!')
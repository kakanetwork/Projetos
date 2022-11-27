
# Entrada de Dados para o Calculo
a = float(input("Informe o Valor de A: "))
b = float(input("Informe o Valor de B: "))
c = float(input("Informe o Valor de C: ")) 

# Condição N°1 - Onde A deve ser diferente de Zero para a Realização da Fórmula
if a != 0:

    #Fórmula de Delta, X1 e X2 
    delta = b**2 - 4*a*c 
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)

    # Condição N°2 - Onde a depender do Resultado de Delta, teremos ou não o Resultado da Equação X
    if delta > 0:
        print(f'\nSua equação teve como Resultado {x1:.2f}, {x2:.2f}!')
    elif delta == 0:
        print(f'\nSua equação teve como Resultado {x1:.2f}, para ambas as raizes!')
    else:
        print(f'\nO valor de Delta foi: {delta}, o delta é negativo, Logo Equação não possui raízes reais.')
else:
    print('\nInforme um número diferente de Zero para A!')
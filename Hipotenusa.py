# Entrada de Dados
A = int(input("Informe o Primeiro Cateto: "))
B = int(input("Informe o Segundo Cateto: "))

# Condição para que ambas as variavéis sejam Positivas
if A > 0 and B > 0:

    # Fórmula da Hipotenusa: √(A² + b²)
    hip = (A**2 + B**2)**(1/2)
    print(f'\nO resultado da Hipotenusa é: {hip:.2f}\n')
else:
    print("\nUtilize apenas Números Positivos para o Calculo!")
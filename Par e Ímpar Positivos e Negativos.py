
# Entrada de Dados
A = int(input("Informe o Valor: "))

# Condições para Descobrir a Propriedade do Valor

if A % 2 == 0 and A > 0:
    # Onde o Número será Par se o Resto da sua Divisão por 2 for igual a Zero
    print("O valor informado é um número Par Positivo")

elif A % 2 == 0 and A < 0:
    # Onde o número será positivo quando A > 0 e Negativo quando A < 0
    print("O valor informado é um número Par Negativo")

elif A % 2 == 1 and A > 0:
    # E Se o resto da divisão por 2 for igual a 1, o número será impar
    print("O valor informado é um número Impar Positivo")

elif A % 2 == 1 and A < 0:
    print("O valor informado é um número Impar Negativo")
    
else:
    # E Caso o valor informado seja igual a Zero, será considerado Nulo!
    print("O valor informado é um número Nulo")
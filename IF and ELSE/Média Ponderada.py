# Entrada de Dados
nota1 = int(input("\nInforme a Primeira nota: "))
nota2 = int(input("Informe a Segunda nota: "))
peso1 = float(input("\nInforme o Primeiro Peso: "))
peso2 = float(input("Informe o Segundo Peso: "))

# Condição onde as notas devem ser Números entre 0 e 100 e os Pesos devem ser Maiores ou igual a Zero
if nota1 >0 and nota1 <= 100 and nota2 >0 and nota2 <= 100 and peso1 >= 0 and peso2 >= 0:

    # Cálculo da Média Ponderada, onde multiplica as notas pelo peso e divide pela soma dos pesos
    media = (nota1*peso1 + nota2*peso2)/(peso1+peso2)
    if media >= 60:
        print(f'\nsua média foi {media}, Parabéns está Aprovado!\n')
    elif media < 20:
        print(f'\nsua média foi {media}, está Reprovado!\n')
    else:
        print(f'\nsua média foi {media}, pode fazer a Prova Final!\n')
else:
    print('\nNota não permitida!\n')
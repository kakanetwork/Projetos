nota1 = int(input("\nInforme a Primeira nota: "))
nota2 = int(input("Informe a Segunda nota: "))

if nota1 >0 and nota1 <= 100 and nota2 >0 and nota2 <= 100:
    media = (nota1*2 + nota2*3)/5
    if media >= 60:
        print(f'\nsua média foi {media}, Parabéns está Aprovado!\n')
    elif media < 20:
        print(f'\nsua média foi {media}, está Reprovado!\n')
    else:
        print(f'\nsua média foi {media}, pode fazer a Prova Final!\n')
else:
    print('\nNota não permitida!\n')

# Entrada de Dados
ano = int(input("Informe um ano entre 1900 - 2100: "))

# Condição N°1 - Onde o valor informado seja dentro da faixa de 1900 - 2100
if ano >= 1900 and ano <= 2100:

    # Condição N°2 - Onde o ano será bissexto se o resto da sua divisão por 4, for igual a Zero
    if ano % 4 == 0:
        print('Seu ano é bissexto')
    else:
        print("Seu Ano não é Bissexto")
else:
    print("Informe um ano dentro da faixa de 1900 - 2100")
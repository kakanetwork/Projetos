
# Entrada das variavéis
ang1 = str(input('Informe a Primeira Palavra do Anagrama: '))
ang2 = str(input('Informe a Segunda Palavra do Anagrama: '))
var1, var2 = ang1.upper(), ang2.upper()
qnt2 = len(ang2)
# O anagrama só existe se a quantidade de caracteres das duas palavras forem iguais
if len(ang1) == qnt2:
    cont = 0
    # Cont1 = -1 para que dentro do while, ele pegue o ultimo caracter
    cont1 = -1
    cont2 = 1
    cont3 = 0

    # while que repete x vezes, onde x = tamanho da palavra
    while cont1 <= qnt2:

        # O anagrama só existe quando todas as letras existentes em VAR1 existem em VAR2
        caracter = var2[cont:cont2]
        # após pegar cada digito, ele procura esse digito dentro da VAR2
        anagrama = var1.find(caracter)
        cont += 1
        cont1 += 1
        cont2 += 1

        # Quando find não encontra o digito, ele tem resultado -1, por isso o if só deve funcionar -
        # - quando find for diferente de -1, significa que ele encontrou o digito dentro de VAR2
        if anagrama != -1:
            # Após isso ele adiciona +1 no cont3
            cont3 += 1

    # após finalizar o while, a condição verifica se cont3 é igual ao tamanho da VAR1
    # onde cont3 = a quantidade de digitos que VAR2 possui dentro de VAR1
    # logo se cont3 for igual ao tamanho da palavra, VAR1 e VAR2 são anagramas    
    if cont3 == qnt2:
        print(f'Sua palavra é um anagrama')
    else:
        print(f'{ang1} Não é Anagrama de {ang2}')
else:
    print(f'{ang1} Não é Anagrama de {ang2}')
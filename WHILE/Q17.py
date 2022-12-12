valor = float(input('Informe o valor a ser sacado: R$'))
valor1 = valor
nota = 100
total = 0
ced_moe = 'Cédula(s)'
cents = ''
soma = 0 # USEI PARA TENTAR SAIR DO PROBLEMA DE VALOR1 == 0, POIS QUANDO CHEGAVA NAS MOEDAS DE 0.01, ELE NÃO CONSIDERAVA VALOR == 0
while True:
    if valor1 >= nota:
        total += 1
        soma += nota
        valor1 -= nota
    else:
        if total > 0:
            print(f'{total} {ced_moe} de R${nota:.2f} {cents}')
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        elif nota == 2:
            ced_moe = 'Moeda(s)'
            nota = 1
        elif nota == 1:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'
            nota = 0.50
        elif nota == 0.50:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.25
        elif nota == 0.25:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.10
        elif nota == 0.10:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.05
        elif nota == 0.05:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.01
        total = 0
        if valor1 == 0 or soma == valor: # USEI A SOMA DE TODAS AS MOEDAS PARA SAIR DO PROBLEMA Q ESTAVA TENDO AQUI, NEM SEMPRE O VALOR ERA == 0!
            break # E O WHILE FICAVA EM LOOPING INFINITO, EXISTE OUTRA FORMA DE CONTORNAR ISSO ALÉM DA SOMA QUE UTILIZEI?
valor = float(input('Insira um valor inicial da aplicação:'))
taxa = float(input('Insira o valor de taxa mensal desejado:'))
porcen = taxa
invest = valor 
qtd_mes = 1
ano = 11
if valor and taxa != 0:
    while qtd_mes <= ano:
        qtd_mes +=1
        porcen = (1+taxa/100)
        rend_m = invest * porcen
        invest = rend_m + valor
        if qtd_mes > ano:
             print(f'\nO valor inicial aplicado foi: {valor}')
             print(f'A taxa foi: {taxa:.2f}%')
             print(f'O saldo do investimento após 1 ano: {invest:.2f}')
             A = str(input('\nDeseja calcular mais um ano? [S] ou [N]: '))
             if A == 'S':
                ano += 12
                print(ano)
             else:
                print('Fim da Simulação de Juros Compostos! ')
else:
    print('Informe um Número para Valor Inicial e Taxa Mensal diferentes de ZERO!')
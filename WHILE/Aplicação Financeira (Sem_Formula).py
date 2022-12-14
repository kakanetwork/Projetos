
# ESTE PROGRAMA FAZ A O RETORNO DE UM INVESTIMENTO COM CONTAS DE MÊS A MÊS DURANTE 1 ANO
######## SEM UTILIZAR FÓRMULA DE JUROS COMPOSTOS ########
simb = '%'
valor = float(input('Insira um valor inicial da aplicação: R$')) # Informe o valor da aplicação mensal 
taxa = float(input('Insira o valor de taxa mensal desejado: ')) # Informe a Porcentagem de Rendimento Mensal
porcen = taxa
invest = valor 
qtd_mes = 1 # Mês inicial, desconsiderado inicialmente
ano = 11 # Onde o ano tem 11 meses + o mês inicial = 12 meses

if valor and taxa != 0: # Condição onde os valores informados devem ser diferentes de ZERO!

    while qtd_mes <= ano: # Estrutura de Repetição para o calculo de Mês a Mês durante 1 ano
        qtd_mes +=1
        porcen = (1+taxa/100) # Transformação da taxa informada (float) para Porcentagem
        rend_m = invest * porcen # Calculo Principal, onde o Investimento inicial é Multiplicado Pela Taxa
        invest = rend_m + valor # E após isso é somado + Aplicação Mensal do Mês atual

        if qtd_mes > ano: # Condição para que quando chegue o 12° Mês, informe o valor total investido durante 1 ano
             print(f'\nO valor inicial aplicado foi: {valor}') 
             print(f'A taxa foi: {taxa:.2f}%')
             print(f'O saldo do investimento após 1 ano: {invest:.2f}')

             A = str(input('\nDeseja calcular mais um ano? [S] ou [N]: ')) # Condição para caso deseja-se calcular +1 ano em cima do ano Anterior
             if A == 'S':
                ano += 12 # Se for verdadeira a afirmação ele somara +12 meses ao ano, para repetição do while
                print(ano)

             else:
                print('Fim da Simulação de Juros Compostos! ')
else:
    print('Informe um Número para Valor Inicial e Taxa Mensal diferentes de ZERO!')
val = int(input('Informe o Valor inicial da P.G: '))
raz = float(input('Informe a Razão da P.G: '))
qnt = int(input('Quantos termos vc deseja encontrar: '))
posi = int(input(f'Informe a Posição do valor que você quer saber\n(A posição deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
Pg = val
cont = 1
numposi = 0
soma = 0
if val != 0 and qnt != 0 and raz != 0:
    while cont <= qnt:
        print(f'{Pg:.2f}', end = ' , ')
        soma = Pg + soma
        Pg *= raz
        cont += 1
        if cont == posi and posi <= qnt:
            numposi = Pg
    print('FIM DA P.G!')       
    print(f'\nA soma da P.G é igual á {soma}!')
    print(f'O número correspondente a {posi}° Posição na P.G, é o {numposi}!')
    if raz > 1: print('E Sua P.G é crescente!')
    elif 0 < raz < 1: print('E Sua P.G é Descrescente!')
    elif raz == 1: print('E Sua P.G é constante!')
    else: print('E Sua P.G é oscilante!')
else: print('Insira um valor diferente de 0!')

val = int(input('Informe o Valor inicial da P.A: '))
raz = int(input('Informe a Razão da P.A: '))
qnt = int(input('Quantos termos vc deseja encontrar: '))
posi = int(input(f'Informe a Posição do valor que você quer saber\n(A posição deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
prim=val
soma=0
cont=1
numposi=0
while cont <= qnt:
     print(prim, end=' , ')
     soma = prim + soma
     prim+=raz
     cont+=1
     if cont == posi and posi <= qnt:
         numposi = prim
print('FIM DA P.A!')       
print(f'\nA soma da P.A é igual á {soma}!')
print(f'O número correspondente a {posi}° Posição na P.A, é o {numposi}!')
if raz > 0:
     print('E Sua P.A é crescente!')
elif raz < 0:
     print('E Sua P.A é Descrescente!')
else:
     print('E Sua P.A é constante!')
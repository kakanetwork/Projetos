val = int(input('Informe o Valor inicial da P.A: '))
raz = float(input('Informe a Razão da P.A: '))
qnt = int(input('Quantos termos vc deseja encontrar: '))
posi = int(input(f'Informe a Posição do valor que você quer saber\n(A posição deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
p_a=val
soma=0
cont=1
numposi=0
while cont <= qnt:
     print(p_a, end=' , ')
     soma = p_a + soma
     p_a+=raz
     cont+=1
     if cont == posi and posi <= qnt:
         numposi = p_a
print('FIM DA P.A!')       
print(f'\nA soma da P.A é igual á {soma}!')
print(f'O número correspondente a {posi}° Posição na P.A, é o {numposi}!')
if raz > 0: print('E Sua P.A é crescente!')
elif raz < 0: print('E Sua P.A é Descrescente!')
else: print('E Sua P.A é constante!')
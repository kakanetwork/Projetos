val = int(input('Informe um valor parar iniciar a P.A: '))
raz = float(input('Agora informe a razão da P.A: '))
qnt = int(input('Quantos termos quer encontrar na P.A? '))
posi = int(input(f'Agora informe a posição do valor que deseja verificar\n(Lembrando que o valor deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
pa=val
soma=0
cont=1
posi=0
for x in range(cont,qnt+1):
     print(pa, end=' , ')
     soma = pa + soma
     pa+=raz
     cont+=1
     if cont == posi and posi <= qnt:
         posi = pa
print('P.A encerrada!')       
print(f'A soma da P.A é igual á {soma}!')
print(f'O número correspondente a {posi}° posição na P.A é = {posi}!')
if raz > 0: 
    print('P.A crescente!')
elif raz < 0: 
    print('P.A descrescente!')
else: 
    print('P.A constante!')
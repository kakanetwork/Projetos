num = int(input('Informe um Número [0 - Para Encerrar]: '))
menor = num
maior = num
soma = 0
qnt = 0
while num != 0:
    soma += num
    qnt += 1
    if maior < num:
        maior = num
    elif menor > num:
        menor = num
    num = int(input('Informe um Número [0 - Para Encerrar]: '))
print(f'A média dos valores é: {soma/qnt}\nO maior número é: {maior}\nO menor número é: {menor}')
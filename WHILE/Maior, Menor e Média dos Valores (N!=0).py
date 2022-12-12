
# Programa onde Encontra o Menor e Maior Número informado, além da sua Média!

num = int(input('Informe um Número [0 - Para Encerrar]: '))
menor = num
maior = num
soma = 0
qnt = 0

while num != 0: # Estrutura de Repetição para que o Input seja acionado sempre que digitar qualquer Número que seja diferente de ZERO
    soma += num
    qnt += 1

    if maior < num: # Condição N°1 - Onde vai salvar o Maior Número Informado
        maior = num
    elif menor > num: # Condição N°2 - Onde vai salvar o Menor Número Informado
        menor = num
    num = int(input('Informe um Número [0 - Para Encerrar]: '))

    # Dentro do Print, a Média já é calculado em {soma/qnt}
print(f'A média dos valores é: {soma/qnt}\nO maior número é: {maior}\nO menor número é: {menor}')
c = 1
cont1 = 0
cont2 = 0
while c <= 5:
    sex = str(input('Informe se você é Homem [H] ou Mulher [M]: '))
    if sex == 'H':
         idadeho = int(input('Informe a sua Idade: '))
         idade1 = idadeho + idade1
         cont1 += 1
         print(idade1)
    elif sex == 'M':
         idademu = int(input('Informe a sua Idade: '))
         idade2 = idademu + idade2
         cont2 += 1
    else: print('Informe [H] para Homem ou [M] para Mulher!')
    c += 1
print (f'A Média das idades foi > {mediaho} para os Homens e {mediamu} para as Mulheres!')
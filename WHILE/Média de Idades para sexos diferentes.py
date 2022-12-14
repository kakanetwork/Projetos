
# Média de idades para Homens e Mulheres

cont1 = 0
sex = 'A'
cont2 = 0
idade1 = 0
idade2 = 0

while sex != 'S': # Estrutura de Repetição para que continue a menos que a resposta seja 'S' - Sair

    sex = str(input('Informe se você é Homem [H] ou Mulher [M] ou quer Sair [S]: '))

    if sex == 'H': # Condição N°1 - Quando o input for H (homem), ele solicitara a sua idade
         idadeho = int(input('Informe a sua Idade: '))
         idade1 = idadeho + idade1 # E ira Armazenar a mesma dentro da Variavel idade1
         cont1 += 1 # Faz o cont +1 para saber quantos homens informaram a sua idade

    elif sex == 'M': # Condição N°2 - Quando o input for M (Mulher), ele solicitara a sua idade
         idademu = int(input('Informe a sua Idade: '))
         idade2 = idademu + idade2 # Segue a mesma ideia da Condição N°1
         cont2 += 1

    else: print('Informe [H] para Homem ou [M] para Mulher ou [S] para Sair!')

# Calculo da Média de idades separadamente
mediaho = idade1 // cont1 
mediamu = idade2 // cont2
print (f'A Média das idades foi > {mediaho} para os Homens e {mediamu} para as Mulheres!')
print (f'\nA Média geral foi: {(idade1+idade2)/(cont1+cont2)}')
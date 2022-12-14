# Lendo a massa inicial
massa_inicial = int(input('Informe a massa inicial (gramas): '))

massa_final    = massa_inicial
tempo_segundos = 0

# Calculando a massa final e o tempo decorrido
while massa_final >= 0.5:
   massa_final = massa_final / 2
   tempo_segundos += 50

# Calculando as horas
tempo_horas    = tempo_segundos // 3600
tempo_segundos = tempo_segundos % 3600

# Calculando os minutos
tempo_minutos  = tempo_segundos // 60
tempo_segundos = tempo_segundos % 60

# Exibindo os dados
print(f'\nMassa inicial : {massa_inicial} gramas')
print(f'\nMassa final ..: {massa_final} gramas')
print(f'\nTempo Total ..: {tempo_horas} h, {tempo_minutos} m, {tempo_segundos} s')
# INCOMPLETO #

''' valor = float(input('Informe o valor a ser sacado: R$'))
valor1 = valor
nota = 100
total = 0
ced_moe = 'Cédula(s)'
cents = ''
soma = 0
while True:
    if valor1 >= nota:
        total += 1
        soma += nota
        valor1 -= nota
    else:
        if total > 0:
            print(f'{total} {ced_moe} de R${nota:.2f} {cents}')
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        elif nota == 2:
            ced_moe = 'Moeda(s)'
            nota = 1
        elif nota == 1:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'
            nota = 0.50
        elif nota == 0.50:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.25
        elif nota == 0.25:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.10
        elif nota == 0.10:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.05
        elif nota == 0.05:
            ced_moe = 'Moeda(s)'
            cents = 'Centavo(s)'            
            nota = 0.01
        total = 0
        if valor1 == 0 or soma == valor:
            break  '''


# INCOMPLETO #
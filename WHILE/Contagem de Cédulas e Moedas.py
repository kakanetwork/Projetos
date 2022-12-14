# Lendo o valor do saque
while True:
    valor = float(input('Informe o valor: '))
    if valor >= 0: break
    
# Separando a parte inteira da parte decimal
parte_cedulas = int(valor)
parte_moedas  = int((valor - parte_cedulas) * 100)

# Calculando e exibindo a quantidade de cédulas/moeda
cedulas_100   = parte_cedulas // 100
parte_cedulas = parte_cedulas % 100

cedulas_050   = parte_cedulas // 50
parte_cedulas = parte_cedulas % 50

cedulas_020   = parte_cedulas // 20
parte_cedulas = parte_cedulas % 20

cedulas_010   = parte_cedulas // 10
parte_cedulas = parte_cedulas % 10

cedulas_005   = parte_cedulas // 5
parte_cedulas = parte_cedulas % 5

cedulas_002   = parte_cedulas // 2
cedulas_001    = parte_cedulas % 2  

moedas_050    = parte_moedas // 50  # 0.50 * 100
parte_moedas  = parte_moedas % 50

moedas_025    = parte_moedas // 25  # 0.25 * 100
parte_moedas  = parte_moedas % 25

moedas_010    = parte_moedas // 10  # 0.10 * 100
parte_moedas  = parte_moedas % 10

moedas_005    = parte_moedas // 5  # 0.05 * 100
moedas_001    = parte_moedas % 5

if (cedulas_100 > 0): print(f'{cedulas_100:>5} cédulas de R$ 100,00')
if (cedulas_050 > 0): print(f'{cedulas_050:>5} cédulas de R$  50,00')
if (cedulas_020 > 0): print(f'{cedulas_020:>5} cédulas de R$  20,00')
if (cedulas_010 > 0): print(f'{cedulas_010:>5} cédulas de R$  20,00')
if (cedulas_005 > 0): print(f'{cedulas_005:>5} cédulas de R$   5,00')
if (cedulas_002 > 0): print(f'{cedulas_002:>5} cédulas de R$   2,00')
if (cedulas_001 > 0): print(f'{cedulas_001:>5} moedas  de R$   1,00')
if (moedas_050 > 0):  print(f'{moedas_050:>5} moedas  de R$   0,50')
if (moedas_025 > 0):  print(f'{moedas_025:>5} moedas  de R$   0,25')
if (moedas_010 > 0):  print(f'{moedas_010:>5} moedas  de R$   0,10')
if (moedas_005 > 0):  print(f'{moedas_005:>5} moedas  de R$   0,05')
if (moedas_001 > 0):  print(f'{moedas_001:>5} moedas  de R$   0,01')
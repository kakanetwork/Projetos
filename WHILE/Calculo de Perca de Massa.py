
# Programa que Calcula um determinado material radioativo que perde metade de sua massa a cada 50 segundos
# E informa o tempo final para que a massa seja menor/igual a 0,5g 

# Declaração de Variavéis 
mi = float(input('determine o peso inicial em gramas: '))
mf = mi
var = 0
hora = 0
min = 0
seg = 0

while mf >= 0.5: # Estrutura de Repetição para que o programe pare quando a Massa for menor/igual a 0,5g
    mf = mf/2 # Calculo da perca de metade do peso
    var +=1

# Calculos do tempo para que se cumpra o objetivo
hora = (var*50)/3600 
min = (var*50)/60
seg = (var*50)%60

print(f'\nMassa inicial: {mi}g\nMassa final: {mf:.3f}g') 
print(f'Tempo em horas: {hora:.0f} Horas\nTempo em Minutos: {min:.1f} Min\nTempo em Segundos {seg:.0f} Seg\n')


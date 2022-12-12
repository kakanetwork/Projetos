mi = float(input('determine o peso inicial em gramas: '))
mf = mi
var = 0
hora = 0
min = 0
seg = 0
while mf >= 0.5:
    mf = mf/2
    var +=1
hora = (var*50)/3600
min = (var*50)/60
seg = var*50
print(f'\nMassa inicial: {mi}g\nMassa final: {mf:.2f}g') 
print(f'Tempo em horas: {hora:.2f} Horas\nTempo em Minutos: {min:.2f} Min\nTempo em Segundos {seg:.2f} Seg\n')


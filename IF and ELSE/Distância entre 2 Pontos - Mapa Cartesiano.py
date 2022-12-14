# Entrada de dados dos 4 Pontos 
ya = float(input("\nInforme a Coordenada de A em Y: "))
xa = float(input("\nInforme a Coordenada de A em X: "))
yb = float(input("\nInforme a Coordenada de B em Y: "))
xb = float(input("\nInforme a Coordenada de B em X: "))

# Calculo Matemático para descobrir a Distância entre 2 Pontos
Dab = (((xb - xa)**2)+((yb - ya)**2))**(1/2) 
# Utiliza a Seguinte Fórmula: √((Xb - Xa)² + (Yb - Ya)²)

print(f"\nA distância entre os pontos {xa, ya} e {xb, yb} é de: {Dab:.2f}")
# Utiliza a função :.2f para a formatação do número em 2 casas Decimais
x = int(input('Informe a coordenada inicial de x:'))
y = int(input('Informe a coordenada inicial de y:'))
var1, var2 = x, y
qnt_mov = 0
qnt_val = 0
while True:
    movimento = str(input('\nInsira para onde o robô deve se deslocar: '))
    movimento = movimento.lower()
    qnt_mov +=1
    if movimento == 'u':
        y += 1
        qnt_val += 1
    elif movimento == 'd':
        y -= 1
        qnt_val += 1
    elif movimento == 'r':
        x += 1
        qnt_val += 1
    elif movimento == 'l':
        x -= 1
        qnt_val += 1
    elif movimento == 'o':
        y += 1
        x -= 1
        qnt_val += 1
    elif movimento == 'n':
        y += 1
        x +=1
        qnt_val += 1
    elif movimento == 'e':
        y -= 1
        x += 1
        qnt_val += 1
    elif movimento == 'w':
        y -= 1
        x -= 1
        qnt_val += 1
    else:
        print('\nInforme uma letra válida!\n-> U (cima) - D (baixo) - R (direita) - L (esquerda)')
        print('-> O (cima-esquerda) - N (cima-direita) - E (baixo-direita) e W (baixo-esquerda)\n')
    print(f'A posição Inicial foi -> {var1, var2}\nA posição Final é -> {x,y}')
    print(f'Quantidade de Movimentos -> {qnt_mov}\nQuantidade de Movimentos Válidos -> {qnt_val}')

    if var1 > 0 and var2 > 0:
         print(f'O robô Começou no primeiro quadrante nas coordenadas -> {var1,var2}')
    elif var1 < 0 and var2 < 0:
         print(f'O robô Começou no Terceiro quadrante nas coordenadas -> {var1,var2}')
    elif var1 < 0 and var2 > 0:
         print(f'O robô Começou no Segundo quadrante nas coordenadas -> {var1,var2}')
    elif var1 > 0 and var2 < 0:
         print(f'O robô Começou no Quarto quadrante nas coordenadas -> {var1,var2}')
    else:
         print(f'O robô inicial não está definido em um Quadrante -> {var1,var2}')
    if x > 0 and y > 0:
         print(f'O robô terminou no primeiro quadrante nas coordenadas -> {x,y}')
    elif x < 0 and y < 0:
         print(f'O robô terminou no Terceiro quadrante nas coordenadas -> {x,y}')
    elif x < 0 and y > 0:
         print(f'O robô terminou no Segundo quadrante nas coordenadas -> {x,y}')
    elif x > 0 and y < 0:
         print(f'O robô terminou no Quarto quadrante nas coordenadas -> {x,y}')
    else:
         print(f'O robô final não está definido em um Quadrante -> {x,y}')
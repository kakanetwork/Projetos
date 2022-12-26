x = int(input('\nInforme a Coordenada inicial de X: '))
y = int(input('Informe a Coordenada inicial de Y: '))
var1, var2 = x, y
movi_val = 0
u, d, r, l, o, n, e, w = 0, 0, 0, 0, 0, 0, 0, 0
while True:
    print('\n',end='='*100)
    movi = str(input('\n\nInsira para onde o robô deve se deslocar: '))
    movi = movi.upper()
    if movi == 'U':
        y += 1
        movi_val += 1
        u += 1
    elif movi == 'D':
        y -= 1
        movi_val += 1
        d += 1
    elif movi == 'R':
        x += 1
        movi_val += 1
        r += 1
    elif movi == 'L':
        x -= 1
        movi_val += 1
        l += 1
    elif movi == 'O':
        y += 1
        x -= 1
        movi_val += 1
        o += 1
    elif movi == 'N':
        y += 1
        x +=1
        movi_val += 1
        n += 1
    elif movi == 'E':
        y -= 1
        x += 1
        movi_val += 1
        e += 1
    elif movi == 'W':
        y -= 1
        x -= 1
        movi_val += 1
        w += 1
    else:
        print('\nInforme uma letra válida!\n-> U (cima) - D (baixo) - R (direita) - L (esquerda)')
        print('-> O (cima-esquerda) - N (cima-direita) - E (baixo-direita) e W (baixo-esquerda)\n')
    print(f'A posição Inicial foi -> {var1, var2}\nA posição Final é -> {x,y}')
    print(f'Quantidade de Movimentos Válidos -> {movi_val}')
    print(f'Os movimentos válidos executados foram:\n{u}x Cima, {d}x Baixo, {r}x Direita, {l}x Esquerda, {o}x Noroeste, {n}x Nordeste, {e}x Sudeste, {w}x Sudoeste')
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
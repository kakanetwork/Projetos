x = int(input('\nInforme a coordenada inicial de x: '))
y = int(input('Informe a coordenada inicial de y: '))
var1, var2 = x, y
qnt_val = 0
u, d, r, l, o, n, e, w = 0, 0, 0, 0, 0, 0, 0, 0
while True:
    print('\n',end='='*100)
    movimento = str(input('\n\nInsira para onde o robô deve se deslocar: '))
    movimento = movimento.lower()
    if movimento == 'u':
        y += 1
        qnt_val += 1
        u += 1
    elif movimento == 'd':
        y -= 1
        qnt_val += 1
        d += 1
    elif movimento == 'r':
        x += 1
        qnt_val += 1
        r += 1
    elif movimento == 'l':
        x -= 1
        qnt_val += 1
        l += 1
    elif movimento == 'o':
        y += 1
        x -= 1
        qnt_val += 1
        o += 1
    elif movimento == 'n':
        y += 1
        x +=1
        qnt_val += 1
        n += 1
    elif movimento == 'e':
        y -= 1
        x += 1
        qnt_val += 1
        e += 1
    elif movimento == 'w':
        y -= 1
        x -= 1
        qnt_val += 1
        w += 1
    else:
        print('\nInforme uma letra válida!\n-> U (cima) - D (baixo) - R (direita) - L (esquerda)')
        print('-> O (cima-esquerda) - N (cima-direita) - E (baixo-direita) e W (baixo-esquerda)\n')
    print(f'A posição Inicial foi -> {var1, var2}\nA posição Final é -> {x,y}')
    print(f'Quantidade de Movimentos Válidos -> {qnt_val}')
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
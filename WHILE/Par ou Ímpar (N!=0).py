rep = 1
while rep != 0:
    rep = int(input('informe o Número: '))
    rep = abs(rep)
    if rep != 0:
        if rep%2 == 0: print('Seu Número é Par!\n')
        else: print('Seu Número é Impar!\n')
    else: print('Você Encerrou o Programa!')
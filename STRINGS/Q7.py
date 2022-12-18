var = str(input('Insira uma palavra: '))
qnt = len(var)
cont = 1
cont1 = 1
cont2 = 0
cont3 = qnt-1
while cont1 <= (qnt*2):
    if cont <= qnt:
        print(var[cont2:cont])
        cont+=1
    elif cont > qnt:
        print(var[cont2:cont3])
        cont3-=1
    cont1+=1
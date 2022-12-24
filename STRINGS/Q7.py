var = str(input('Insira uma palavra: '))
qnt = len(var)
cont = 1
cont1 = 1
cont2 = qnt-1
while cont1 <= (qnt * 2):
    if cont <= qnt:
        print(var[:cont])
        cont+=1
    elif cont > qnt:
        print(var[:cont2])
        cont2-=1
    cont1+=1
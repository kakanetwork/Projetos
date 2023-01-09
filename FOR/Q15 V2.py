bin = input('informe um número binário: ')
var1 = bin[::-1]
dec = 0
cont = 0 
while cont < len(var1):
    if var1[cont] == '1':
        dec += 2 ** cont
    cont+=1
print(f'O valor decimal de {bin} é = {dec}')
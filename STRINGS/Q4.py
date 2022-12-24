var = input('Informe um Valor: ')
Var1 = var.replace(' ', '').upper()
posi = len(Var1)-1
cont = 0
while posi > cont and Var1[cont] == Var1[posi]:
    posi -= 1
    cont += 1
if Var1[cont] == Var1[posi]: print(f"\n> {var} < é um Palíndromo!\n")
else:
     print(f"\n> {var} < não é um Palíndromo! ")
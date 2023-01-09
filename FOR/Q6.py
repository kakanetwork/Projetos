vogais = 'aáâeéêiíoóôuú'
palavra = str(input('Informe a palavra para encontrarmos as vogais: '))
var1 = palavra.lower()
qnt = 0
aux1 = 0
aux2 = 1
for x in range(len(var1)):
        caracter = var1[aux1:aux2]
        find = vogais.find(caracter)
        aux1 += 1
        aux2 += 1
        if find != -1:
            qnt+=1
print(f'A palavra {palavra} informada possui {qnt} vogais!')
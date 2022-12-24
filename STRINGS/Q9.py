palavra_chave = 'MENINO'
aux = palavra_chave
qnt = len(palavra_chave)
acertos = 0
qnterros = 6
tentativas = ''

while True:
    letra = str(input('\nInforme uma letra [Poderá errar até 6x]: ')).upper()
    repet = tentativas.find(letra)
    forca = palavra_chave.find(letra)
    if repet != -1:
        print(f'\nA letra {letra} já foi informado, tente outra!\n')
    elif forca != -1:
        palavra_chave = palavra_chave.replace(letra,'')
        qnt = len(palavra_chave)
        print(f'\nVocê acertou! faltam -> {qnt} letras')
        acertos += 1
    else:
        print(f'\nVocê Errou! tem direito a mais -> {qnterros-1} erro(s).')
        qnterros -= 1
    tentativas += letra
    if qnterros == 0 or qnt == 0:
         break

if qnt == 0:
    print(f'\nPARABÉNS! VOCÊ GANHOU, A PALAVRA ERA -> {aux}\n')
elif qnterros == 0:
    print(f'\nVOCÊ FOI ENFORCADO! Tente Novamente.\n')
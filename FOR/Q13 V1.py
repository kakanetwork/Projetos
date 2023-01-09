senha_padrao = 'swordfish'
while True:
    password = input('Digite uma senha: ')
    if password == senha_padrao:
        print('Senha Correta!\n')
        break
    else: 
        print('A senha está incorreta, tente novamente!\n')
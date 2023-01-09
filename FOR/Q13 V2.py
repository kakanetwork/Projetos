senha_padrao = 'swordfish'
password = input('Digite uma senha: ')
for cont in range(100000000000):
    if password == senha_padrao:
        print('Senha Correta!\n')
        break
    else: 
        password = input('\nSenha incorreta!\nDigite uma senha: ')

# Entrada de Dados
cpf = int(input('\nInforme o seu CPF: '))
scpf = str(cpf) # CPF convertido para String, será necessário
qnt = len(scpf)

# Condição para que o CPF só tenha 11 Digitos 
if qnt == 11:
    # Designação de Variavéis para While e algumas Auxiliares
    posi = 0 # Posi e Posi1 Vai servir para desmembrar o cpf número por número
    posi2 = 1 
    cont1 = 0 # Cont1 e qntdig Vai servir de contador para o While
    qntdig = 9 
    multiplicador = 10 # Vai servir de multiplicador dos digitos validadores
    soma = 0 # Vai servir para a soma dos valores após a multiplicação
    dig_1v = 0 # Dig_1v e Dig_2v vai servir para armazenamento dos dois digitos validadores
    dig_2v = 0

    while cont1 < qntdig: 
        caracter = scpf[posi:posi2] # Realizando o desmembramento do CPF

        # Calculo: Cada número do CPF * N (n = 10, mas a cada número -1, até atingir 2)
        mult = int(caracter) * multiplicador # Realizando o Primeiro calculo de validação
        # Calculo: Após a multiplicação de cada um, soma-se os resultados
        soma += mult # Realizando o segundo calculo da validação 

        posi += 1
        cont1 += 1
        posi2 += 1
        multiplicador -= 1 # Multiplicador diminui 1 a cada número do cpf, até atingir 2

        # Condição: quando while chegar na sua última volta
        if cont1 == qntdig:
            # Calculo: a soma dos números é multiplicado por 10 e tirado o resto por 11
            dig_2v = (soma * 10)%11 

            # Dig_verificador são variavéis para armazenar a onde se encontra os digitos -
            # - de Verificação no CPF (os dois últimos)
            dig_verificador1 = scpf[9:10]
            dig_verificador2 = scpf[10:]

            # Condição: até aqui temos a verificação do Primeiro Digito Verificador
            # Agora iremos para a verificação do Segundo Digito Verificador
            if str(dig_2v) == dig_verificador1 and qntdig == 9:

                # Para o segundo digito ser calculado, as variavéis precisam mudar os seus valores
                dig_1v = dig_2v
                posi = 0
                cont1 = 0
                posi2 = 1
                multiplicador = 11 # Agora multiplicador começa em 11, invés de 10
                soma = 0
                qntdig = 10 # O contador do while inicia em 10, invés de 9

    # Aqui terminamos o calculo dos dois digitos, e verificamos se eles correspondem aos do CPF            
    if str(dig_1v) == dig_verificador1 and dig_verificador2 == str(dig_2v):
        print(f'\nO CPF: {cpf} É VÁLIDO!\n')
    else:
        print(f'\nO CPF: {cpf} É INVÁLIDO!\n')
else:
    print('\nInforme um CPF com 11 Caracteres [Somente os Números]!\n')
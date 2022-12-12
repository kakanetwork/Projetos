
# Programa que Informa todos os Valores Primos até o Número Informado

valor = int(input('Informe um Número: '))
if valor > 1:
    aux = 1
    while aux <= valor:
        cnt_divi = 0
        divi = 1
        while divi <= valor:
            if aux % divi == 0: cnt_divi += 1
            if cnt_divi > 3: break
            divi += 1
        if cnt_divi == 2: print(aux, end=',')
        aux += 1
    print('FIM!')
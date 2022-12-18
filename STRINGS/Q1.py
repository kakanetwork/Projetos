
# Definindo as vogais acentuadas
vogais = 'aáâeéêiíoóôuú'
var = str(input('Informe a Palavra na qual deseja encontrar as vogais: '))
var1 = var.lower()
qnt = 0
cont = 1
cont1 = 0
cont2 = 1

# while que repete x vezes, onde x = Todas as possibilidades de vogais
while cont <= len(vogais):

        # Retira vogal por vogal e joga a variavél 'caracter'
        caracter = vogais[cont1:cont2]
        print(caracter)
        # Verifica se existe caracter na palavra, onde caracter = cada vogal definida
        find = var1.find(caracter)
        cont += 1
        cont1 += 1
        cont2 += 1

        # Find tem resultado diferente de -1 quando encontra o Caracter dentro da Palavra
        if find != -1:
            # Toda vez que ele encontrar o Caracter, vai adicionar +1 na quantidade
            # onde qnt = quantidade de vogais existentes na palavra
            qnt+=1
print(f'A Palavra {var} possui um total de {qnt} vogais!')

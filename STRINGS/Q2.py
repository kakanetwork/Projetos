var = str(input('Digite uma frase: '))

print(f'A frase que você inseriu foi: {var}\n'); print('Corrigindo os espaços vazios...\n')
var = var.replace(' ', '_')
print(f'A frase corrigida é: {var}'); print('\nFim!')
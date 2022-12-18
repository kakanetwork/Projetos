frase = str(input('Insira uma frase: '))
pant = str(input('Insira a palavra que deseja mudar da frase anterior: '))
pnova = str(input('Insira a palavra que deseja substituir na frase anterior: '))
print(f'A frase antiga era: {frase}'); print(f'A palavra antiga era: {pant}'); print(f'A palavra nova é: {pnova}')
frase = frase.replace(pant, pnova)

print('\nSubstituindo as palavras selecionadas...\n');print(f'A frase nova é: {frase}\n'); print('Fim!')
# Realizada a Entrada dos valores
A = float(input("Informe o Primeiro Valor: "))
B = float(input("Informe o Segundo Valor: "))

# Mostrando as Variavéis antes da Inversão
print(f'Os valores de {A} [Antes da Inversão] e {B} [Antes da troca]!')
# Realizando a inversão de Variavéis
A, B = B, A
print(f'\n...Invertendo...\n\nOs valores de {A} [Depois da Inversão] e {B} [Depois da troca]!')
# Utiliza a função \n para o Pulo de Uma linha
# Utiliza a função (f'{A}') para a inserção da variavel dentro da string sem necessidade de vírgula

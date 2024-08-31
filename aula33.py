# Exercicio 1
numero = input('Digite um número inteiro: ')

try:
    numero_int = float(numero)
    if numero_int % 2 == 0: 
        print('É par')
    else:
        print('É impar')
except:
    print('Digte um numero inteiro...')
    
# Exercicio 2
try:
    horario = int(input('Digite o horario local: '))
    if horario >= 0 and horario <= 11:
        print('Bom dia')
    elif horario >= 12 and horario <= 17:
        print('Boa Tarde')
    elif horario >= 18 and horario <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite uma hora valida')  
    
# Exercicio 3
nome = input('Digite seu nome: ')
nome_tamanho = len(nome)
if nome_tamanho >= 1:
    if nome_tamanho <= 4:
        print('Seu nome é pequeno')
    elif nome_tamanho >= 5 and nome_tamanho <= 6:
        print('Seu nome é normal')
    else: 
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
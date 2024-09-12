# Exercicio com while

nome = input('Digite seu nome e sobrenome: \n')
iterando = 0
novo_nome = ''
while iterando < len(nome):
    letra = f'*{nome[iterando]}'
    novo_nome += letra
    iterando += 1
novo_nome += '*'
print(novo_nome)
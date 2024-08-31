# While

condicao = True
while condicao:
    name = input('Digite seu nome: ')
    
    if name == 'Sair' or name == 'sair':
        break
    
    print(f'Seu nome é {name}')

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)
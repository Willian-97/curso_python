# Operadores in e not in
nome = 'Willian'
print(nome[2]) # String são iteraveis
print('W' in nome) # Verificando se W esta em nome
print('z' not in nome) # Verificando se  z não esta em nome

user_name = input('Digite seu nome: ')
search = input('Digite o que deseja encontra: ')

if search in user_name:
    print(f'{search} esta em {user_name}')
elif search not in user_name: 
    print(f'{search} não esta em {user_name}')
else:
    print('Erro...')

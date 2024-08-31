# Operador not (invertendo a expressão logica)
print(not True)
print(not False)

senha = input('Senha: ')
if not senha:
    print('Voce não digitou nada...')
elif senha == '1234':
    print('Entrou')
else:
    print('Senha incorreta!')

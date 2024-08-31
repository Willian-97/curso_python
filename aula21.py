# Operador and

entrada = input('Deseja entrar [E]? ')
senha_digitada = input('Digite sua senha: ')
senha_aceita = 123456

if entrada == 'E' and senha_aceita == int(senha_digitada):
    print('Entrou')
else:
    print('Saiu')
    
    
# Valores falsy 
print(bool(0.0))
print(True and False and True)
print(True and True and True)
print(True and 0 and True)

if True and 1:
    if True and 0.0:
        print('Tudo ok')
    else:
        print('erro')
else:
    if True and True:
        if '' and False:
            print('Tudo ok')
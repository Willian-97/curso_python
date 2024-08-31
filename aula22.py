# operador or
entrada = input('Deseja entrar [E]? ')
senha_digitada = input('Digite sua senha: ')
senha_aceita = 123456

if entrada == 'E' or entrada == 'e' and senha_aceita == int(senha_digitada):
    print('Entrou')
else:
    print('Saiu')
    
# Avaliação de curto circuito
print(True or False or False)
nome = input('Digite seu nome: ') or 'Usuario'
senha = input('digite sua senha: ') or 1234
print(senha)
print(nome)
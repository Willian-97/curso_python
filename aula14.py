# Usando o metodo format()
a = 'Willian'
b = 'Gasparini'
c = 10.555555

# ordem dos parametros
formatado = 'Nome: {}, Sobrenome: {}, Valor: {:.2f}'.format(a, b, c)
# indice dos parametros
formatado2 = 'Olá meu nome é {0} e tenho R$:{2:.2f} na carteira'.format(a, b, c)
# Parametro nomeado
formatado3 = 'Var 2: {valor2} Var 3: {valor3} Var 1: {valor}'.format(valor = a, valor2 = b, valor3 = c)

print(formatado) 
print(formatado2)
print(formatado3)

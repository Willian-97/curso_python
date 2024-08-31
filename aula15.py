# Funcao input

# nome = input('Digite seu nome: ')
# print(f'Seu nome é {nome}')
# # exibi a variavel
# print(f'Seu nome é {nome=}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
# Usar a coerção quando a checagem for feita, para evitar erros
numero_1_int = int(numero_1)
numero_2_int = int(numero_2)

print(f'A soma dos números é {numero_1_int + numero_2_int}')

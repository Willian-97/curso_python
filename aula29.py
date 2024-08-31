# try e except
numero = input('Vou dobrar o número que vc degitar: ')

try:
    print(f'Convertendo o número {numero} para float...')
    numero_float = float(numero)
    print(f'O número dobrado é: {numero_float * 2}')
except:
    numero_str = numero.capitalize()
    print(f'{numero_str}, não é um número')
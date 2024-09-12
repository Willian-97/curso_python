# Exercicio calculadora

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite a operação [+ - / *]: ')
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Digite apenas numeros')
        continue
    
    operadores_validos = '+-/*'
    
    if operador not in operadores_validos:
        print('Operador invalido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operdor')
        continue
    
    print('Realizando o calculo. Confira seu resultado abaixo')
    if operador == '+':
        print(numero_1_float + numero_2_float)
        
    elif operador == '-':
        print(numero_1_float - numero_2_float)
        
    elif operador == '/':
        print(numero_1_float / numero_2_float)
        
    elif operador == '*':
        print(numero_1_float * numero_2_float)
        
    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
    
    if sair is True:
        break
# f-strings

variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:-<10}')
print(f'{variavel:0<10}')
print(f'{variavel:^10}')
print(f'O Hexadecimal foi {100.1515151:0=+10,.1f}')
print(f'O Hexadecimal foi {255:06X}')

nome = 'Will'
age = 27
sex = 'Masculino'
print(f'Olá, meu nome é {nome}, eu tenho {age} anos e sou do sexo {sex}')
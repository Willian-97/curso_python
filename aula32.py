# Flag, is, is not, none

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else: 
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
    
if passou_no_if is not None:
    print('Passou no if')
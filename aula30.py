# Variaveis, constantes e complexidade de codigo
velocidade = 66
localizacao_do_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = localizacao_do_carro >= (LOCAL_1 - 1) and localizacao_do_carro <= (LOCAL_1 + 1)
multado = carro_multado_radar_1 and vel_carro_pass_radar_1 

if vel_carro_pass_radar_1: 
    print('O carro passou no radar 1')
    
if multado:
    print('Carro foi multado no radar 1')
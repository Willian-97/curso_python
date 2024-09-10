# while com continue
contador = 0
while contador < 100:
    contador += 1
    
    if contador == 6: 
        print('Pulei o 6')
        continue
    
    if contador >= 10 and contador <= 20:
        print('Pulei', contador)
        continue
    
    
    if contador > 40:
        break
    

    print(contador)

print('Acabou')
hemoglobina = float(input())
genero = int(input())

if (genero == 1 and hemoglobina < 12.2) or (genero == 2 and hemoglobina < 12.6):
    print('Baja')
elif (genero == 1 and hemoglobina <= 16.6) or (genero == 2 and hemoglobina <= 15):
    print('Normal')
elif (genero == 1 and hemoglobina > 16.6) or (genero == 2 and hemoglobina > 15):
    print('Alta')
else:
    print('No es posible generar la alerta')
""" Un centro de salud desea iniciar una investigación relacionada con la detección temprana de enfermedades asociadas con el nivel de hemoglobina.

El rango normal de hemoglobina se define generalmente como 12,2 a 16,6 gramos (g) de hemoglobina por decilitro (dL) de sangre para los hombres y 12,6 a 15 g/dL para las mujeres.

Para el estudio en mención de desea inicialmente diseñar e implementar un algoritmo que dado el valor de la hemoglobina en g/dL y el género de un paciente (1: Masculino, 2: Femenino) indique el rango en el que se encuentra (alta, normal, baja), como lo indica la siguiente tabla.

Hemoglobina Género Alerta

< 12,2 Masculino Baja

< 12,6 Femenino Baja

[12,2 – 16,6] Masculino Normal

[12,6 – 15] Femenino Normal

>16,6 Masculino Alta

>15 Femenino Alta



Además, si el valor del género no se encuentra dentro de los valores esperados (1 o 2) debe mostrar el siguiente mensaje: “No es posible generar la alerta”

Entrada Esperada   Salida Esperada

10 1         Baja

17 2         Alta

14 2         Normal

16 0         No es posible generar la alerta """

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
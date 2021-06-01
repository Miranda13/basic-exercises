""" Un centro de salud desea iniciar una investigación relacionada con la detección temprana
de enfermedades asociadas con el nivel de hemoglobina.
El rango normal de hemoglobina se define generalmente como 12,2 a 16,6 gramos (g)
de hemoglobina por decilitro (dL) de sangre para los hombres y 12,6 a 15 g/dL para las
mujeres.
La investigación en su primera fase, verificará el nivel de hemoglobina en un conjunto de
N pacientes. Se le ha solicitado a usted diseñar un algoritmo que para cada uno de los N
pacientes a partir de su género (1: Masculino, 2: Femenino) y nivel de hemoglobina actual
contabilice 3 alertas como se describe en la siguiente tabla.

Hemoglobina Género Alerta
< 12,2 Masculino Baja
< 12,6 Femenino Baja
[12,2 – 16,6] Masculino Normal
[12,6 – 15] Femenino Normal
> 16,6 Masculino Alta
> 15 Femenino Alta
Si el valor del género no se encuentra dentro de los valores esperados (1 o 2) debe
solicitar el género nuevamente hasta que sea un dato válido.
El algoritmo debe indicar lo siguiente:
 Cuantos hombres tienen alerta “Baja”
 Cuantos hombres tienen alerta “Alta”
 Cuantos hombres tienen alerta “Normal”.
 Cuántas mujeres tienen alerta “Baja”
 Cuántas mujeres tienen alerta “Alta”
 Cuántas mujeres tienen alerta “Normal”.
Entrada Esperada    Salida Esperada
                    5 1 0 2 0 1 1
10 1
17 2
14 2
16 1
14 1
 """
pacientes = int(input())
i = 0
hBaja = 0
hAlta = 0
hNormal = 0
mBaja = 0
mNormal = 0
mAlta = 0
while (i < pacientes):
    hemoglobina= float(input())
    genero = int(input())
    while(genero != 1 and genero != 2):
        genero = int(input())
    if (genero == 1):
        if (hemoglobina < 12.2):
            hBaja += 1
        elif (hemoglobina <= 16.6):
            hNormal += 1
        elif (hemoglobina > 16.6):
            hAlta += 1
    elif (genero == 2):
        if (hemoglobina < 12.6):
            mBaja += 1
        elif (hemoglobina <= 15):
            mNormal += 1
        elif (hemoglobina > 15):
            mAlta += 1    
    i += 1
print(hBaja, hAlta, hNormal, mBaja, mAlta, mNormal)   
    
    
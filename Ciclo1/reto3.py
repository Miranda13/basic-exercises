""" Un centro de salud desea iniciar una investigación relacionada con la detección temprana
de enfermedades asociadas con el nivel de hemoglobina.
El rango normal de hemoglobina se define generalmente como 12,2 a 16,6 gramos (g)
de hemoglobina por decilitro (dL) de sangre para los hombres y 12,6 a 15 g/dL para las
mujeres.
La investigación en su segunda fase, además de verificar el nivel de hemoglobina en un
conjunto de N pacientes (primera fase), generará datos estadísticos que apoyen a los
profesionales en el área en la toma de decisiones certeras. Se le ha solicitado a usted
diseñar un algoritmo que para cada uno de los N pacientes a partir de su género (1:
Masculino, 2: Femenino) y nivel de hemoglobina actual contabilice 3 alertas como se
describe en la siguiente tabla.
Hemoglobina Género Alerta
< 12,2 Masculino Baja
< 12,6 Femenino Baja
[12,2 – 16,6] Masculino Normal
[12,6 – 15] Femenino Normal
> 16,6 Masculino Alta
> 15 Femenino Alta

Si el valor del género no se encuentra dentro de los valores esperados (1 o 2) debe
solicitar nuevamente ambos valores hasta que se ingrese un género válido.
El algoritmo debe indicar lo siguiente:
 ¿Cuál es la hemoglobina promedio para el género masculino y su alerta
correspondiente?
 ¿Cuál es la hemoglobina promedio para el género femenino y su alerta
correspondiente?
 ¿Cuántos hombres y mujeres están por encima del promedio?
 ¿Cuántos hombres y mujeres están por debajo del promedio?
 ¿Cuántos hombres y mujeres igualan promedio?
Los promedios deben estar formateado a 2 cifras decimales. Además, si no se tienen
registros de hemoglobina de un género, su promedio debe ser 0.00.

Entrada Esperada
5
10 1
17 2
14 2
16 1
14 1

Salida Esperada
13.33 Normal
15.50 Alta
2 1
1 1
0 0 """
pacientes = int(input())
i = 0
mujeres = []
hombres = []

def promedio(array):
    if len(array) == 0:
        return 0.00
    else:
        suma = 0
        for item in range(len(array)):
            suma = suma + array[item]
        return round(suma/len(array), 2)

def contar(nivel,array):
    mayor = 0
    menor = 0
    iguales = 0
    for valor in range(len(array)):
        if (array[valor] > nivel):
            mayor += 1
        elif (array[valor] < nivel):
            menor += 1
        else:
            iguales += 1
    return [mayor, menor, iguales]

def rango(valor, bajo, normal, alto):
    if (valor < bajo):
        return "Baja"
    elif (valor <= normal):
        return "Normal"
    elif (valor > alto):
        return "Alta"

while (i < pacientes):
    datos = input().split(" ")
    genero = int(datos[1])
    hemoglobina = float(datos[0])
    while(genero != 1 and genero != 2):
        datos = input().split(" ")
        genero = int(datos[1])
        hemoglobina = float(datos[0])   
    if (genero == 1):
        hombres.append(hemoglobina)
    elif (genero == 2):
        mujeres.append(hemoglobina)
    i += 1

promedioMujer = promedio(mujeres)
promedioHombre = promedio(hombres)

rangoMujer = rango(promedioMujer, 12.6, 15, 15)
rangoHombre = rango(promedioHombre, 12.2, 16.6, 16.6)

contarHombres = contar(promedioHombre, hombres)
contarMujeres = contar(promedioMujer, mujeres)

print(format(promedioHombre, ".2f"),rangoHombre)
print(format(promedioMujer, ".2f"),rangoMujer)
print(contarHombres[0],contarMujeres[0])
print(contarHombres[1],contarMujeres[1])
print(contarHombres[2],contarMujeres[2])
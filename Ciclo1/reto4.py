""" Un centro de salud desea iniciar una investigación relacionada con la detección temprana de enfermedades asociadas con el nivel de hemoglobina.
 El rango normal de hemoglobina se define generalmente como 12,2 a 16,6 gramos (g) de hemoglobina por decilitro (dL) de sangre para los hombres y 12,6 a 15 g/dL para las mujeres.
 La investigación se encuentra en su tercera fase de implementación, en la cual se verifica
 el nivel de hemoglobina en un conjunto de N pacientes durante una semana completa.
 Los datos son almacenados en una estructura de datos como la siguiente:

            Género  Dia 1   Dia 2   Dia 3   Dia 4   Dia 5   Dia 6   Dia 7 
Paciente 1  1       13      13,5    14      13      15      11      12,4
Paciente 2  1       14,3    11,4    15,3    12,1    8,6     11,5    12
Paciente N  2       12,4    10,1    11,4    13,2    12,3    11,8    10,9

 En donde la primera columna corresponde al género del paciente (1: Masculino, 2: Femenino), y de la segunda a la octava columna corresponden a las lecturas de hemoglobina durante los 7 días de la semana.
 En las fases anteriores de la investigación se ha generado una alerta del nivel de hemoglobina teniendo en cuenta la siguiente tabla:

Hemoglobina Género Alerta
< 12,2 Masculino Baja
< 12,6 Femenino Baja
[12,2 – 16,6] Masculino Normal
[12,6 – 15] Femenino Normal
> 16,6 Masculino Alta
> 15 Femenino Alta

Para apoyar la conclusión de esta nueva fase, se le ha solicitado a usted diseñar un algoritmo que para cada uno de los N pacientes:
- Lea el género.
- Lea los 7 valores de hemoglobina correspondientes a cada uno de los días de la semana.
- Genere un vector en el cual se almacene el resultado de la alerta a partir de su género (1: Masculino, 2: Femenino) y el promedio de las 7 lecturas.

El algoritmo debe indicar lo siguiente:

- ¿Cuál es el género, número y alerta del paciente con el promedio de lecturas más alto? Si hay más de un paciente, se toma la información del primero que se encuentre.
- ¿Cuál es el género, número y alerta del paciente con el promedio de lecturas más bajo? Si hay más de un paciente, se toma la información del primero que se encuentre.
- ¿Cuántos hombres y cuantas mujeres se encuentran dentro del estudio?
Los promedios deben estar formateados a 2 cifras decimales.
 
Entrada Esperada
5
1 10.0 12.0 11.3 7.5 12.3 12.5 13.2
2 17.0 12.3 14.1 15.5 11.0 10.0 15.3
2 11.0 16.0 13.3 9.5 12.6 12.4 13.4
1 10.3 10.0 12.3 11.5 11.3 15.5 17.1
1 10.1 12.0 11.3 6.5 12.3 16.5 15.2
Salida Esperada
2 13.60 Normal 
1 11.26 Baja 
3 2 """

numeroPacientes = int(input())

def promedio(array):
    if len(array) == 0:
        return 0.00
    else:
        suma = 0
        for item in range(len(array)):
            suma = suma + array[item]
        return round(suma/len(array), 2)

def rango(genero, valor):
    if (genero == 1):
        bajo = 12.2
        normal = 16.6
        alto = 16.6   
    elif (genero == 2):
        bajo = 12.6
        normal = 15
        alto = 15
    if (valor < bajo):
        return "Baja"
    elif (valor <= normal):
        return "Normal"
    elif (valor > alto):
        return "Alta"

hombres = 0
mujeres = 0

for i in range(numeroPacientes):
    datos = input().split(" ")
    paciente = []
    paciente.append(int(datos[0]))
    for hemo in range(1, len(datos)):
        paciente.append(float(datos[hemo]))
    if (i == 0):
        promedioInicial = promedio(paciente[1:len(paciente)])
        if (paciente[0] == 1):
            hombres += 1
        if (paciente[0] == 2):
            mujeres += 1
        menor = [paciente[0], promedioInicial]
        mayor = [paciente[0], promedioInicial]
    else:
        promedioPaciente = promedio(paciente[1:len(paciente)])
        if (promedioPaciente < menor[1]):
            menor = [paciente[0], promedioPaciente]
        if (promedioPaciente > mayor[1]):
            mayor = [paciente[0], promedioPaciente]
        if (paciente[0] == 1):
            hombres += 1
        if (paciente[0] == 2):
            mujeres += 1

print(mayor[0], format(mayor[1], ".2f"), rango(mayor[0], mayor[1]))
print(menor[0], format(menor[1], ".2f") ,rango(menor[0], menor[1]))
print(hombres, mujeres)
    


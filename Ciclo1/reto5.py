import csv

hombres = 0
mujeres = 0
pacientes = []

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def promedio(array):
    if len(array) == 0:
        return 0.00
    else:
        suma = 0
        for item in range(len(array)):
            suma = suma + array[item]
        return suma/len(array)


with open('data.csv', newline='') as File:
    reader = csv.reader(File)
    firstline = True
    for index, row in enumerate(reader):
        if firstline:  # skip first line
            firstline = False
            continue
        paciente = [row[0], row[1], row[2], int(row[3]), promedio(
            [float(row[4]), float(row[5]), float(row[6]), float(row[7])])]
        pacientes.append(paciente)
        if (index == 1):
            if (paciente[1] == "M"):
                hombres += 1
            if (paciente[1] == "F"):
                mujeres += 1
        else:
            if (paciente[1] == "M"):
                hombres += 1
            if (paciente[1] == "F"):
                mujeres += 1

datos = input().split(" ")
nivel = float(datos[1])
sede = int(datos[0])

mayor = []
menor = []
indicador = 0
iguales = 0
mayores = 0
menores = 0
sedes = [0]*15

for paciente in pacientes:
    if paciente[3] == 1:
        sedes[0]+=1
    if paciente[3] == 2:
        sedes[1]+=1
    if paciente[3] == 3:
        sedes[2]+=1
    if paciente[3] == 4:
        sedes[3]+=1
    if paciente[3] == 5:
        sedes[4]+=1
    if paciente[3] == 6:
        sedes[5]+=1
    if paciente[3] == 7:
        sedes[6]+=1
    if paciente[3] == 8:
        sedes[7]+=1
    if paciente[3] == 9:
        sedes[8]+=1
    if paciente[3] == 10:
        sedes[9]+=1
    if paciente[3] == 11:
        sedes[10]+=1
    if paciente[3] == 12:
        sedes[11]+=1
    if paciente[3] == 13:
        sedes[12]+=1
    if paciente[3] == 14:
        sedes[13]+=1
    if paciente[3] == 15:
        sedes[14]+=1
    #Otra cosa    
    if paciente[4] > nivel:
        mayores += 1
    elif paciente[4] < nivel:
        menores += 1
    else:
        iguales += 1
    if indicador == 0:
        if paciente[3] == sede:
            indicador += 1
            mayor = paciente
            menor = paciente
    else:
        if paciente[3] == sede:
            if(paciente[4] > mayor[4]):
                mayor = paciente
            if(paciente[4] < menor[4]):
                menor = paciente

def rango(valor, bajo, normal, alto):
    if (valor < bajo):
        return "Baja"
    elif (valor <= normal):
        return "Normal"
    elif (valor > alto):
        return "Alta"

print(mayor[0], mayor[1], mayor[2], rango(mayor[4], 12.6, 15, 15))
print(menor[0], menor[1], menor[2], rango(menor[4], 12.2, 16.6, 16.6))
print(mayores, menores, iguales)
print("M", hombres)
print("F", mujeres)
for index, sede in enumerate(sedes):
    print(index+1, sede)

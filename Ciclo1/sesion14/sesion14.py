"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""

#Actividad 1

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"

def actividad1(matriz):
    cuadrada = True
    for item in matriz:
        if(len(item) != len(matriz)):
            cuadrada = False
    if(cuadrada):
        for i in range (len(matriz)):
            print(matriz[i][i])
    else:
        print("La matriz no es cuadrada")

#actividad1([[1,1,1],[2,7,1],[3,3]])

#Actividad 2
#
#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#

#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc
def actividad2():
    tamanio = int(input("Por favor ingrese el tamaño de la matriz: "))
    matriz = []
    contador = 0
    while (contador < tamanio):
        while True:
            fila = input(f"Ingrese los valores de la fila {contador+1}: ").split(" ")
            if (len(fila) == tamanio):
                break
        matriz.append(fila)
        contador +=1
    print(matriz[0])
    for item in range(tamanio):
        print(matriz[item][0], end=" ")
    print()  
    print(matriz[1][1])

#actividad2()

""" Determinar si una matriz es un cuadro mágico, es decir si la suma de todas sus filas, columnas
y diagonales son iguales """

def esCuadrada(matriz):
    for item in matriz:
        if(len(item) != len(matriz)):
            return False
    return True

def esMagico(array):
    valor = array[0]
    for suma in array:
        if (valor != suma):
            return False
    return True

def cuadradoMagico(matriz):
    if(esCuadrada(matriz)):
        sumas = []
        sumaDiagonal = 0
        sumaDiagonal2 = 0
        for item in range(len(matriz)):
            sumaDiagonal = sumaDiagonal + matriz[item][item]
            sumaDiagonal2 = sumaDiagonal2 + matriz[item][len(matriz)-1-item]
            sumaColum = 0
            sumaFila = 0
            for item2 in range(len(matriz[item])):
                sumaColum = sumaColum + matriz[item][item2]
                sumaFila = sumaFila + matriz[item2][item] 
            sumas.extend([sumaColum, sumaFila])
        sumas.extend([sumaDiagonal,sumaDiagonal2])
        if (esMagico(sumas)):
            print("Es mágico")
        else:
            print("No es mágico")
    else:
        print("La matriz no es cuadradada")


cuadradoMagico([
    [ 2, 7, 6],
    [ 9, 5, 1],
    [ 4, 3, 8] ])

cuadradoMagico([ [ 1, 15, 14, 4],
    [ 12, 6, 7, 9],
    [ 8, 10, 11, 5],
    [13, 3, 2, 16] ])

""" 1. Agregar
    2. Mostrar
                3. Remover x nombre
                4. Remover x posici?n
                5. Tama?o Lista
                6. Ordenar Ascendente
                7. Ordenar Descendente
                8. Consultar x posición
                9. Agregar en la posicion (x) """
lista = []

def agregar(elemento):
    lista.append(elemento)

def mostrar():
    print(lista)

def removerXNombre(nombre):
    lista

def removerXPosicion(posicion):

def menu():
    print(''' 1. Agregar 
    2. Mostrar 
    3. Remover x nombre 
    4. Remover x posición 
    5. Tamaño Lista 
    6. Ordenar Ascendente
    7. Ordenar Descendente
    8. Consultar x posición
    9. Agregar en la posicion (x)
    0. Salir''')
    election = int(input())
    return election
        
def main():
    election = menu()
    while(election != 0):
        if (election == 1):
            valor = int(input())
            agregar(valor)
        election = menu()

main()

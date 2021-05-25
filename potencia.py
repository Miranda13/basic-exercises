""" Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia. """

base = float( input("Escriba la base para la potencia: "))
exponente = int (input("Escriba un entero positivo como exponente: "))
if (exponente > 0):
    total = 1
    while (exponente > 0):
        total = base * total
        exponente -= 1
    print(total)
elif (exponente == 0):
    print(1)
else:
    print("El exponente debe ser positivo") 

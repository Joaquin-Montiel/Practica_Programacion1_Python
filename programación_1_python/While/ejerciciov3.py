#WHILE - Validaciones
#Ejercicio 3: Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

nota = 0

while(nota < 1 or nota > 10):
    nota = int(input("Ingrese una nota (entre 1 y 10): "))
    if (nota < 1 or nota > 10):
        print("La nota no es valida, intente nuevamente.")

print(f"Nota valida. La nota ingresada es {nota}.")

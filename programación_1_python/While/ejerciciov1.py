#WHILE - Validaciones
#Ejercicio 1: Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto.
#  Tendrá intentos indeterminados.

clave_correcta = "Utnfra750"
clave_ingresada = ""

while (clave_ingresada != clave_correcta):
    clave_ingresada = input("Ingrese la clave correcta (mayúscula, minúscula y números): ")
    if (clave_ingresada != clave_correcta):
        print("La clave ingresada no es correcta, intente nuevamente.")

print("Su clave fue validada con éxito.")



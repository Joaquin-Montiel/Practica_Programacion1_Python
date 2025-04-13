#WHILE - Validaciones
#Ejercicio 2: Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

clave_correcta = "Utnfra750"
clave_ingresada = ""
intentos_maximos = 3
intentos_realizados = 0

while (clave_ingresada != clave_correcta and intentos_realizados < intentos_maximos):
    clave_ingresada = input("Ingrese la clave correcta (mayúscula, minúscula y números): ")
    intentos_realizados += 1
    if (clave_ingresada != clave_correcta):
        print(f"La clave ingresada no es correcta, le quedan {intentos_maximos - intentos_realizados} intentos.")

if (clave_ingresada == clave_correcta):
    print("Su clave fue validada con éxito.")
else:
    print("La clave no es correcta. No tiene más intentos. Acceso denegado.")
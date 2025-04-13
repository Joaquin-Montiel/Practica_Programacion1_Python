#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 10: Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

contador_vueltas = 0
ingreso_maximo = 10
suma = 0

print("Por favor ingrese entre 5 y 10 numeros.")
while(contador_vueltas < ingreso_maximo):
    numero_entrada = int(input(f"Ingrese el número {contador_vueltas + 1}: "))
    suma += numero_entrada
    contador_vueltas += 1
    if (contador_vueltas >= 5):
        entrada = input("Desea ingresar otro número? (s/n)")
        if (entrada != "s"):
            break

if (contador_vueltas < 5):
    print(f"Error, solo se ingresaron {contador_vueltas} número. Se deben ingresar al menos 5.")
elif (contador_vueltas > 0):
    promedio = suma / contador_vueltas
    print(f"Se ingresaron {contador_vueltas}.")
    print(f"La suma de los números ingresados es {suma}.")
    print(f"El promedio de los números ingresados es {promedio}.")
else:
    print("No se ingresaron números.")




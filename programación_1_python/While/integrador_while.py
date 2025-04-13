#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio Integrador: Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
#La suma acumulada de los números negativos.
#La suma acumulada de los números positivos.
#La cantidad de números negativos ingresados.
#El promedio de los números positivos.
#El número positivo más grande.
#El porcentaje de números negativos ingresados, respecto del total de ingresos.

total_ingresos = 0
respuesta = "s"
suma_positivos = 0
suma_negativos = 0
contador_negativos = 0
contador_positivos = 0
positivo_mas_grande = None

while (respuesta == "s"):
    numero_entrada = int(input("Ingrese un número: "))
    total_ingresos += 1

    if (numero_entrada < 0):
        suma_negativos += numero_entrada
        contador_negativos += 1
    elif (numero_entrada > 0):
        suma_positivos += numero_entrada
        contador_positivos += 1
        if positivo_mas_grande is None or numero_entrada > positivo_mas_grande:
            positivo_mas_grande = numero_entrada
    
    respuesta = input("Desea seguir ingresando números? (s/n): ").lower()

if (contador_positivos > 0):
    promedio_positivos = suma_positivos / contador_positivos
else:
    promedio_positivos = 0

if (total_ingresos > 0):
    porcentaje_negativos = (contador_negativos / total_ingresos * 100)
else:
    porcentaje_negativos = 0

print(f"La suma de los números positivos es {suma_positivos}, y la de los números negativos es {suma_negativos}.")
print(f"La cantidad de números negativos ingresados es {contador_negativos}.")
print(f"El promedio de los números positivos es {promedio_positivos}.")
print(f"El número positivo más grande ingresado es {positivo_mas_grande}.")
print(f"El porcentaje de los números negativos es {porcentaje_negativos}")


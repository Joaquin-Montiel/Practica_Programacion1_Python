#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 9:  Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

contador_vueltas = 0
respuesta = "s"
suma = 0

while(contador_vueltas < 5):
    numero_entrada = int(input(f"Ingrese el número {contador_vueltas + 1}: "))
    suma += numero_entrada
    contador_vueltas += 1


while(respuesta == "s"):
    entrada = input("Desea ingresar números extras? (s/n): ")
    if (entrada == "s"):
        numero_entrada = int(input("Ingrese otro número: "))
        suma += numero_entrada
        contador_vueltas += 1
    else:
        break

    
if (contador_vueltas > 0):
    promedio = suma / contador_vueltas
    print(f"Se ingresaron {contador_vueltas}")
    print(f"La suma de los números ingresados es {suma} y su promedio es {promedio}.")
else:
    print("No se ingresaron números.")


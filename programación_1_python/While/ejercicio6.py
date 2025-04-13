#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 6: Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

contador_vueltas = 0
suma = 0

respuesta = "s"

while(respuesta == "s"):
    numero_entrada = int(input("Ingrese un numero: "))
    suma += numero_entrada
    contador_vueltas += 1

    respuesta = input("Desea continuar ingresando numeros? (s/n)")

promedio = suma / contador_vueltas

print(f"La suma de los numeros ingresados por el usuario es {suma} y su promedio es {promedio}.")

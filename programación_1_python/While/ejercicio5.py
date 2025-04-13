#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 5: Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.

contador_vueltas = 1
suma = 0

while(contador_vueltas <= 5):
    numero_entrada = int(input("Ingrese un numero: "))
    suma += numero_entrada
    contador_vueltas +=1

promedio = suma / 5
print(f"La suma de los numeros ingresados es {suma}, y su promedio es {promedio}.")


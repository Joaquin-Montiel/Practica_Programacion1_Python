#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 3: Mostrar la suma de los números desde el 1 hasta el 10.

suma = 0
numero = 1

while(numero <= 10):
    #print(numero)
    suma += numero
    numero += 1
    

print(f"La suma de todos los numeros es: {suma}")

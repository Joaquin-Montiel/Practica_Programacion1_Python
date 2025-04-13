#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 4: Mostrar la suma de los números pares desde el 1 hasta el 10.

suma_pares = 0
numero = 1

while(numero <= 10):
    if (numero % 2 == 0):
        #print(numero)
        suma_pares += numero
    numero += 1

print(f"La suma de los numeros pares es: {suma_pares}")


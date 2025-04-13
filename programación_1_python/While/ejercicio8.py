#Guia WHILE
#Contadores - Acumuladores - Máximos y mínimos
#Ejercicio 8: Ingresar 10 números enteros. Determinar el máximo y el mínimo.


contador_vueltas = 0
numero_maximo = None
numero_minimo = None

while(contador_vueltas <= 10):
    contador_vueltas += 1

    numero_entrada = int(input("Ingrese un numero: "))
    if (numero_maximo is None or numero_entrada > numero_maximo):
        numero_maximo = numero_entrada

    if (numero_minimo is None or numero_entrada < numero_minimo):
        numero_minimo = numero_entrada

print(f"El numero máximo ingresado es {numero_maximo}, y el numero minímo ingresado es {numero_minimo}")
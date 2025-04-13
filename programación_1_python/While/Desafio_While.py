#📌 Desafío: Encuesta Tecnológica en UTN Technologies
#UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, 
# con el objetivo de revolucionar el mercado.
#Las tecnologías en evaluación son:
# 🔹 Inteligencia Artificial (IA)
# 🔹 Realidad Virtual/Aumentada (RV/RA)
# 🔹 Internet de las Cosas (IOT)
#Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar 
# ciertas métricas.
#🔹 Recolección de Datos
#Cada empleado encuestado deberá proporcionar la siguiente información:
# ✔️ Nombre
# ✔️ Edad (debe ser 18 años o más)
# ✔️ Género (Masculino, Femenino, Otro)
# ✔️ Tecnología elegida (IA, RV/RA, IOT)
#El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
#🔹 Análisis de Datos
#A partir de las respuestas, se deben calcular las siguientes métricas:
#1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
#2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
#Su género no sea Femenino 
#Su edad está entre los 33 y 40 años.
#3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.
#
#🔹 Requisitos del Programa
# ✔️ Los datos deben solicitarse y validarse correctamente.
# ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
# ✔️ Presentar los resultados de manera clara y organizada.

empleado = 0
contador_empleados = 0
edad_empleado_masculino_mayor = None
nombre_empleado_masculino_edad_mayor = None
tecnologia_empleado_masculino_edad_mayor = None
contador_masculinos_votaron_iot_ia_25_50 = 0
porcentaje_no_ia_no_femenino_33_40 = 0
contador_no_femenino_no_ia = 0


while (empleado < 10):
    contador_empleados += 1

    #Carga de los datos
    nombre_empleado = None
    while(nombre_empleado is None or not nombre_empleado.isalpha()):
        nombre_empleado = input("Ingrese su nombre: ")
        if (not nombre_empleado.isalpha()):
            print("El nombre ingresado no es correcto. Intente nuevamente.")

    edad = None
    while (edad is None or edad < 18):
        edad_str = input("Ingrese su edad (mayor de 18): ")
        edad = int(edad_str)
        if  (edad is None or edad < 18):
            print("La edad ingresada no es valida. Intente nuevamente.")

    genero = None
    while(genero is None or not (genero == "Masculino" or genero == "Femenino" or genero == "Otro")):
        genero = input("Ingrese su genero (Masculino, Femenino, Otro): ")
        if not (genero == "Masculino" or genero == "Femenino" or genero == "Otro"):
            print("El genero ingresado no es correcto. Intente nuevamente.")

    tecnologia = None
    while(tecnologia is None or not (tecnologia == "IA" or tecnologia == "RV/RA" or tecnologia == "IOT")):
        tecnologia = input("Ingrese su tecnologia (IA, RV/RA, IOT): ")
        if not (tecnologia == "IA" or tecnologia == "RV/RA" or tecnologia == "IOT"):
            print("El tecnologia ingresado no es correcto. Intente nuevamente.")

    #Analisis de los datos
    if (genero == "Masculino" and (tecnologia == "IA" or tecnologia == "IOT") and (edad >= 25 and edad <= 50)):
        contador_masculinos_votaron_iot_ia_25_50 += 1

    if (genero != "Femenino" and tecnologia != "IA" and (edad >= 33 and edad <= 40)):
        contador_no_femenino_no_ia += 1

    if (genero == "Masculino" and (edad_empleado_masculino_mayor is None or edad > edad_empleado_masculino_mayor)):
        edad_empleado_masculino_mayor = edad
        nombre_empleado_masculino_edad_mayor = nombre_empleado
        tecnologia_empleado_masculino_edad_mayor = tecnologia

    empleado +=1


porcentaje_no_ia_no_femenino_33_40 = contador_no_femenino_no_ia / contador_empleados

print("----------RESULTADOS DE LA ENCUESTA----------")
print("---------------------------------------------")
print(f"1.La cantidad de empleados masculinos entre 25 y 50 años que votaron IA y IOT son \
        {contador_masculinos_votaron_iot_ia_25_50}")
print(f"2.El porcentaje de empleados entre 33 y 40 años que no votaron IA y que no eran de género Femenino fueron \
        {porcentaje_no_ia_no_femenino_33_40}")
print(f"El empleado del género masculino de mayor edad es {nombre_empleado_masculino_edad_mayor},"
    f"con {edad_empleado_masculino_mayor} años y su voto de tecnologia fue para {tecnologia_empleado_masculino_edad_mayor}")





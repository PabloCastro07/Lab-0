# Programa para calcular el Indice de Aridez y clasificar el clima 

# Funcion para calcular
def calcular():
    try:
        # Pedir datos por consola
        P = float(input("Ingrese la precipitacion anual (mm): "))
        T = float(input("Ingrese la temperatura media (°C): "))

        # Formula del indice
        I = P / (T + 10)

        # Mostrar indice
        print("Indice de aridez:", I)

        # Clasificacion
        if I < 5:
            categoria = "Desierto"
        elif I < 10:
            categoria = "Arido"
        elif I < 20:
            categoria = "Semi-arido"
        elif I < 30:
            categoria = "Sub-humedo"
        elif I <= 60:
            categoria = "Humedo"
        else:
            categoria = "Super-humedo"

        print("Clasificacion:", categoria)

    except:
        print("Error: Ingrese numeros validos")

# Llamar la funcion
calcular()

    # Pedir datos al usuario
    # Muestra un mensaje en pantalla pidiendo la precipitacion anual en milimetros. La funcion input() lee lo que el usuario escribe (siempre como texto).
    # #float() convierte ese texto a numero decimal para poder hacer calculos matematicos. El resultado se guarda en la variable "precipitacion". 
precipitacion = float(input("Ingrese la precipitacion total anual (mm): ")) 
    # Hace lo mismo para la temperatura media anual en grados Celsius. Convierte la entrada a decimal y la guarda en la variable "tiempo".
tiempo = float(input("Ingrese la temperatura media anual (°C): "))

    # Calcular el indice
    # Aplica la formula del Indice de Aridez de Lang: IA= P/T+10
    # Se suma 10 a la temperatura para evitar dividir por cero en zonas muy frias y para normalizar el calculo.
    # El resultado se guarda en "aridez".
aridez = (precipitacion / (tiempo + 10))

    # Muestra el resultado
print("El indice de aridez es:", aridez)
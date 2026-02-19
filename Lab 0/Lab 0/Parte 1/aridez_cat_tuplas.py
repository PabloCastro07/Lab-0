    # Pedir datos
    # Solicita que el usuario ingrese AMBOS valores en una sola entrada, separados por coma (ejemplo: 900,18).
    # La funcion input() devuelve todo como un solo texto (string) y se guarda en la variable "datos".
datos = input("Ingrese precipitacion y temperatura separados por coma (ej: 900,18): ")

    # Separar datos
    # El metodo .split(",") divide el texto en una lista de subcadenas, usando la coma como separador.
    # Si el usuario ingreso "900,18", el resultado es la lista ["900", "18"] y esta lista se guarda en "partes".
partes = datos.split(",")

    # Crear tupla
    # La funcion tuple() convierte la lista ["900", "18"] en una tupla ("900", "18").
tupla = tuple(partes)
    
    # Acceder a los valores
    # Accede al primer elemento de la tupla (indice 0, que es "900") usando notacion de corchetes. float() lo convierte de texto a numero decimal.
precipitacion = float(tupla[0])
    
    # Accede al segundo elemento de la tupla (indice 1, que es "18") y lo convierte a decimal. 
temperatura = float(tupla[1])

    # Calcular aridez
aridez = precipitacion / (temperatura + 10)

    # Muestra el Resultado
print("El indice de aridez es:", aridez)

    # Clasificación
if aridez < 5:
        print("Desierto")
elif aridez >= 5 and aridez < 10:
        print("Arido")
elif aridez >= 10 and aridez < 20:
        print("Semiarido")
elif aridez >= 20 and aridez < 30:
        print("Subhumedo")
elif aridez >= 30 and aridez <= 60:
        print("Humedo")
elif aridez > 60:
        print("Superhumedo")
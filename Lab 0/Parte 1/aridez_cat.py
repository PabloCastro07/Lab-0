# Solicita al usuario la precipitacion anual total en milimetros. float() convierte el texto ingresado a numero decimal y guarda el resultado
precipitacion = float(input("Ingrese la precipitacion total anual en mm: "))
# Solicita la temperatura media anual en grados Celsius
temperatura = float(input("Ingrese la temperatura media anual en grados C: "))
    # Calcular el indice 
    # Aplica la formula del Indice de Aridez de Lang: IA= P/T+10
    # Se suma 10 a la temperatura para evitar dividir por cero en zonas muy frias y para normalizar el calculo.
    # El resultado se guarda en "aridez".
aridez = precipitacion / (temperatura + 10)

    #Muestra el resultado
print("El indice de aridez es:", aridez)

    # Clasificar el clima
if aridez < 5:
        print("Desertico")
elif aridez >= 5 and aridez < 10:
        print("Arido")
elif aridez >= 10 and aridez < 20:
        print("Semiarido")
elif aridez >= 20 and aridez < 30:
        print("Semihumedo")
elif aridez >= 30 and aridez <= 60:
        print("Humedo")
elif aridez > 60:
        print("Superhumedo")
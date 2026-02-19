    # Lista para categorias
categorias = []

    # Número de Municipios
municipios = int(input("Ingrese el numero de municipios: "))

    # Ciclo 
for i in range(municipios):
        print("\nMunicipio", i + 1)

        # Pedir datos 
        datos = input("Ingrese precipitacion y temperatura separados por coma (ej: 900,18): ")

        # Separar datos
        partes = datos.split(",")

        # Crear tupla
        partes = datos.split(",")
        tupla = tuple(partes)
        
        # Acceder a los valores 
        precipitacion = float(tupla[0])
        temperatura = float(tupla[1])

        # Calcular aridez
        aridez = precipitacion / (temperatura + 10)

        # Mostrar resultado
        print("El indice de aridez es:", aridez)

        # Clasificacion
        if aridez < 5:
            categoria = "Desierto"
        elif aridez >= 5 and aridez < 10:
            categoria = "Arido"
        elif aridez >= 10 and aridez < 20:
            categoria = "Semiarido"
        elif aridez >= 20 and aridez < 30:
            categoria = "Subhumedo"
        elif aridez >= 30 and aridez <= 60:
            categoria = "Humedo"
        else:
            categoria = "Superhumedo"

        print("Clasificacion:", categoria)

        # Guardar categoria en la lista
        categorias.append(categoria)

    # Lista Completa
print("\nLista:", categorias)

    # Porcentajes
print("\nPorcentaje:")

total = len(categorias)

for categoria in ["Desierto", "Arido", "Semiarido", "Subhumedo", "Humedo", "Superhumedo"]:
        cantidad = categorias.count(categoria)
        porcentaje = (cantidad / total) * 100
        print(categoria, ":", porcentaje, "%")
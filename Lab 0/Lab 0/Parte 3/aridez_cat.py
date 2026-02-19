# Función para los límites del rango semiarido
def limites():
    inferior = 10
    superior = 20
    return inferior, superior

# Funcion para mostrar el rango
def interpretar_semiarido(indice):
    inferior, superior = limites()

    print("Rango Semiarido:", inferior, ",", superior)

    if indice < inferior:
        print("El municipio esta POR DEBAJO del rango semiarido.")
    elif indice > superior:
        print("El municipio esta POR ENCIMA del rango semiarido.")
    else:
        print("El municipio esta DENTRO del rango semiarido.")

# Calcular porcentajes
def calcular_porcentajes(categorias):

    print("\nPorcentaje por categoria:")

    total = len(categorias)

    for categoria in ["Desierto", "Arido", "Semiarido", "Subhumedo", "Humedo", "Superhumedo"]:
        cantidad = categorias.count(categoria)
        porcentaje = (cantidad / total) * 100
        print(categoria, ":", porcentaje, "%")

def categorizar_climas(aridez):

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

    return categoria
    
# Funcion principal
def calcular_aridez():

    # Categorias
    categorias = []

    # Validacion del numero de municipios
    while True:
        municipio = input("Ingrese el numero de municipios: ")

        # Validar que sea numero
        if not municipio.isdigit():
            print("Valor no valido, ingrese un numero entero.")
            continue

        municipios = int(municipio)

        # Validar positivo
        if municipios <= 0:
            print("El número de municipios debe ser positivo.")
            continue

        break

    # Ciclo y manejo de error
    for i in range(municipios):
        print("\nMunicipio", i + 1)

        # Pedir datos
        while True:
            datos = input("Ingrese precipitacion y temperatura separados por coma (ej: 900,18): ")

            # Validar que tenga coma
            if "," not in datos:
                print("Valor no valido, intente nuevamente.")
                continue

            try:
                partes = datos.split(",")
                precipitacion = float(partes[0])
                temperatura = float(partes[1])
                break
            except ValueError:
                print("Los valores deben ser numericos, intente nuevamente.")

        # Calcular aridez
        aridez = precipitacion / (temperatura + 10)

        # Mostrar resultado
        print("El indice de aridez es:", aridez)

        print ("Clasificacion:", categorizar_climas(aridez))

        interpretar_semiarido(aridez)

        # Categorizar el clima
        categoria = categorizar_climas(aridez)
        categorias.append(categoria)

    # Lista Completa
    print("\nLista:", categorias)

    # Calcular porcentajes
    calcular_porcentajes(categorias)

# Llamar la funcion principal
calcular_aridez()
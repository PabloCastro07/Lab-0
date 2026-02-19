# Programa para evaluar el Indice de Aridez en varios municipios

def clasificar_aridez(indice):
    if indice < 5:
        return "Desierto"
    elif indice < 10:
        return "Arido"
    elif indice < 20:
        return "Semiarido"
    elif indice < 30:
        return "Subhumedo"
    elif indice <= 60:
        return "Humedo"
    else:
        return "Superhumedo"


def main():
    categorias = []
    municipios = []

    # Numero de municipios
    n = int(input("Ingrese el numero de municipios a evaluar: "))

    # Ciclo principal
    for i in range(n):
        print("\nMunicipio", i + 1)

        nombre = input("Nombre del municipio: ")
        municipios.append(nombre)

        datos = input("Ingrese precipitacion y temperatura (ej: 900,18): ")
        datos = tuple(map(float, datos.split(",")))

        P = datos[0]
        T = datos[1]

        # Calculo del indice
        indice = P / (T + 10)

        # Clasificacion
        categoria = clasificar_aridez(indice)
        categorias.append(categoria)

        print("Indice de aridez:", round(indice, 2))
        print("Clasificacion:", categoria)

    # Mostrar lista final
    print("\n=== RESULTADOS FINALES ===")
    for i in range(n):
        print(municipios[i], "->", categorias[i])

    # Calculo de porcentajes
    print("\n=== PORCENTAJE POR CATEGORIA ===")

    total = len(categorias)
    lista_categorias = ["Desierto", "Arido", "Semiarido", "Subhumedo", "Humedo", "Superhumedo"]

    for c in lista_categorias:
        cantidad = categorias.count(c)
        porcentaje = (cantidad / total) * 100
        print(c, ":", round(porcentaje, 2), "%")

# Ejecutar programa
main()

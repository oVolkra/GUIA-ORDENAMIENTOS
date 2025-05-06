def ordenar_ascendente():
    """Función para ordenar una lista de nombres de forma ascendente, según la edad."""

    nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
    edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

    for i in range(len(edades) - 1):
        for j in range(i + 1, len(edades)):
            if edades[i] > edades[j]:
                aux_edades = edades[i]
                edades[i] = edades[j]
                edades[j] = aux_edades

                aux_nombres = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombres

    print(edades)
    print(nombres)

ordenar_ascendente()

def ordenar_materias():
    """Función para ordenar las materias por nombre de forma ascendente."
    En caso de encontrar el mismo nombre, ordena por puntos de forma descendente."""
    
    nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
    puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if nombres[i] > nombres[j]:
                aux_nombres = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombres

                aux_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux_puntos
            
            if nombres[i] == nombres[j]:
                aux_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux_puntos
            
    print(nombres)
    print(puntos)

ordenar_materias()                                  
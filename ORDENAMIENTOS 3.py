def ordenar_alumnos():
    """Función que ordena las listas por apellido de manera ascendente, 
    si el apellido es el mismo, ordena por nombre de manera
    ascendente, si el nombre también es el mismo, ordena por nota de manera descendente"""

    estudiantes = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "María", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "María"]
    apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa", "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade", "Loza", "Antares", "Roca", "Perez"]
    nota = [8, 4, 9, 10, 8, 6, 4, 8, 7, 5, 6, 7, 10, 4, 8]

    for i in range(len(apellidos) - 1):
        for j in range(i + 1, len(apellidos)):
            if apellidos[i] > apellidos[j]:
                # intercambio completo
                aux_apellidos = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux_apellidos

                aux_estudiantes = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux_estudiantes

                aux_nota = nota[i]
                nota[i] = nota[j]
                nota[j] = aux_nota

            elif apellidos[i] == apellidos[j] and estudiantes[i] > estudiantes[j]:
                aux_estudiantes = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux_estudiantes

                aux_nota = nota[i]
                nota[i] = nota[j]
                nota[j] = aux_nota

            elif apellidos[i] == apellidos[j] and estudiantes[i] == estudiantes[j] and nota[i] < nota[j]:
                aux_nota = nota[i]
                nota[i] = nota[j]
                nota[j] = aux_nota

    print(estudiantes)
    print(apellidos)
    print(nota)

ordenar_alumnos()



            


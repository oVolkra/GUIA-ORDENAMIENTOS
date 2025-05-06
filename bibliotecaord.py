#Ejercicio 1
def ordenar_ascendente():
    """Función para ordenar una lista de nombres de forma ascendente, según la edad."""

    nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
    edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

    for i in range(len(edades) - 1):
        for j in range(i + 1, len(edades)):
            if nombres[i] > nombres[j]:
                aux_nombres = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombres 
                
                aux_edades = edades[i]
                edades[i] = edades[j]
                edades[j] = aux_edades

    for i in range(len(nombres)):
        print(f"{nombres[i]}: {edades[i]}")

#Ejercicio 2
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
            
    for i in range(len(nombres)):
        print(f"Materia: {nombres[i]} Nota:{puntos[i]} ")

#Ejercicio 3
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

    for i in range(len(estudiantes)):
        print(f"Nombre: {estudiantes[i]} / Apellido: {apellidos[i]} / Nota: {nota[i]}")



            


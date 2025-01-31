def eliminar_duplicados(lista):
    lista_sin_duplicados = set(lista)
    print("Lista sin duplicados: " ,lista_sin_duplicados)

lista= ["hola", "hola", "caracola", "caracola"]
print("La lista con duplicados: "+str(lista))

eliminar_duplicados(lista)
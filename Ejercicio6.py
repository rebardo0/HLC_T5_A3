def crearDiciionario(lista):
    diccionario = {palabra: len(palabra) for palabra in lista}
    return diccionario

lista = ["colombia", "medellin", "paris", "madrid"]

diccionario = crearDiciionario(lista)
print(diccionario)
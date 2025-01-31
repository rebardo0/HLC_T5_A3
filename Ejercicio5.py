def frecuenciaPalabras():
    oracion="eduardo y david. david y eduardo"
    palabras=oracion.split()
    frecuencia={}

    for palabra in palabras:

        if palabra in frecuencia:
            frecuencia[palabra] += 1

        else:
            frecuencia[palabra] = 1
    return frecuencia

devolver = frecuenciaPalabras()
print(devolver)
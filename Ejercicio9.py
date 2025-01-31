lista = {"valeria": 9, "manolo": 7, "triana": 5}

def notas():
    promedio=0
    maximo_estudiante  = ""
    mejor_nota=0

    for name, nota in lista.items():
        if nota > mejor_nota:
            mejor_nota = nota
            maximo_estudiante = name
            promedio += nota/len(lista)
    return "Promedio: ",promedio, "Mejor estudiante: ",maximo_estudiante, "con un ",mejor_nota
print (notas())
def sumaYpromedio():
    numeros=[10,20,30,40,50]
    suma=0

    for i in numeros:
        suma+=i
    print("La suma de los numeros es", suma, "y el promedio es", suma/len(numeros))

sumaYpromedio()
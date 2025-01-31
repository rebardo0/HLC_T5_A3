def eliminar_numeros_pares():
    list = [1,2,3,4,5,5]

    for i in list:

        if i%2==0:
            list.remove(i)
        print(i)
eliminar_numeros_pares()
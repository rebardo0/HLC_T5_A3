def divisores(numeroos):
    divisores = []

    for i in range(1, numeroos + 1):
        
        if numeroos % i == 0:
            divisores.append(i)
    return divisores

numeroos = 28
print(divisores(numeroos)) 
def Max(a, b, c):
    if a > b > c:
        return a
    elif a > c > b:
        return a
    elif a < b < c:
        return c
    else:
        return c 
        


Nombre1 = float(input('Entrez le premier nombre : '))
Nombre2 = float(input('Entrez un deuxième nombre : '))
Nombre3 = float(input('Entrez le troisième nombre : '))

maximum = Max(Nombre1, Nombre2, Nombre3)
print ("le maximum de ces deux nombres est : ", maximum)



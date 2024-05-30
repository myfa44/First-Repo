def Max(a, b):
    if a > b:
        return a
    else:
        return b


Nombre1 = float(input('Entrez un nombre : '))
Nombre2 = float(input('Entrez un autre nombre : '))

maximum = Max(Nombre1, Nombre2)
print ("le maximum de ces deux nombres est : ", maximum)
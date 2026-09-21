#ORDEN ASCENDENTE
lista =[100,99,92,85,74,77,60,98,55,81,75,76,84,95,92]
n = len(lista)
swapped = True
while swapped:
    swapped = False
    for i in range (n-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            swapped=True
print("Orden Ascendente:",lista)            

#ORDEN DECENDENTE
lista =[100,99,92,85,74,77,60,98,55,81,75,76,84,95,92]
n = len(lista)
swapped = True
while swapped:
    swapped = False
    for i in range (n-1):
        if lista[i]<lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            swapped=True
print("Orden Decendente:",lista)   
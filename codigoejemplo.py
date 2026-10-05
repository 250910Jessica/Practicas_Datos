# codigo de ejeplo


import numpy as np

a_list = [1, 2, 3, 4]
an_array = np.array(a_list)
print(an_array)

# Expected output: [1 2 3 4]



# Resultado del análisis
# Complejidad temporal: 
# Crear un array NumPy a partir de una lista de Python requiere un tiempo de O(n), donde n es el número de elementos (n = 4 en el ejemplo). 
# Esto implica asignar memoria para el array y copiar cada elemento. 

# Complejidad espacial: 
# El array resultante almacena n elementos, por lo que ocupa O(n) espacio. Además, 
# la lista de entrada también ocupa O(n) espacio, pero tras la conversión al array, 
# el espacio adicional predominante es el propio array. En la práctica, 
# se puede considerar que el uso total de espacio para la estructura de datos es de O(n).

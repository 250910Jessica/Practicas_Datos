import matplotlib.pyplot as plt

datos = [42, 12, 88, 23, 7, 65, 34, 50]

# Algoritmo de Inserción corregido
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave, j = a[i], i - 1
        while j >= 0 and a[j] > clave:
            comp += 1
            a[j + 1] = a[j]
            j -= 1
        if j >= 0:
            comp += 1
        a[j + 1] = clave
    return a, comp

# Algoritmo de Selección corregido
def seleccion(arr):
    a = arr.copy()
    comp = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        # Intercambio correcto al finalizar la búsqueda del mínimo
        a[i], a[min_idx] = a[min_idx], a[i]  
    return a, comp                        

# Ejecutar ambos algoritmos
lista_ordenada, comp_ins = insercion(datos)
_, comp_sel = seleccion(datos)

# Configuración de la figura y subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.5))

# Gráfico 1: Lista Inicial Desordenada
ax1.bar(range(len(datos)), datos, color='salmon')
ax1.set_title('1.- Lista Desordenada')
ax1.set_ylabel('Valor')

# Gráfico 2: Lista Ordenada
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='green')
ax2.set_title('2.- Lista Ordenada')
ax2.set_ylabel('Valor')

# Gráfico 3: Comparaciones Realizadas
ax3.bar(['Inserción', 'Selección'], [comp_ins, comp_sel], color=["#2397EA", "#ac8059"])
ax3.set_title('3.- Comparaciones Realizadas')
ax3.set_ylabel('Cantidad')

plt.tight_layout()
plt.show()
def calcular_area_triangulo(base,altura):
    area = (base*altura)/2
    return area
resultado = calcular_area_triangulo(10,5)
print(f"El area del triangulo:{resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre},tienes {edad} años.")
saludar_persona("Elena",28 )    


#*/*/*/*/*/*/ EJEMPLOS /*/*/*/*/*/*/*

def calcular_suma(a,b):
    suma = (a+b)
    return suma
resultado = calcular_suma(55,98)
print(f"el resultado de la suma es:{resultado}")    

def libro_favorito_y_serie(libro,serie):
    print(f"Mi libro favorito es {libro} , y mi serie favorita es {serie}.")
libro_favorito_y_serie("Percy Jackson","La casa de papel")    
        
def encabezado_escuela():
    print("INSTITUTO UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DEL ESTADO DE PUEBLA")
encabezado_escuela()

def obtener_nota_minima_aprobatoria():
    print("la nota minima necesaria pra aprobar el curso 6.0")
obtener_nota_minima_aprobatoria()

def evaluar_rendimiento(nota):
    if nota <= 7.0:                    
        nota = "Reprobado"            
    elif nota <= 9.4:                 
        nota = "Aprobado"             
    else:                             
        nota = "Excelente"            
    return nota                       
calificacion = evaluar_rendimiento(10.0)
print(f"El resultado del curso es: {calificacion}")
      
def calcular_promedio_ponderado(evaluacion, libreta):
    calf = evaluacion + libreta
    if calf == 100:
        calf= "Excelente"
    elif calf>= 70:
        calf = "Aprobado"
    else:
       calf = "Reprobado"
    return calf
calificacion_final= calcular_promedio_ponderado(70, 30)
print(f"El resultado final del curso es: {calificacion_final}")

  
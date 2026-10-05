def encabezado_escuela():
    print("INSTITUTO UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DEL ESTADO DE PUEBLA")
encabezado_escuela()

def obtener_nota_minima_aprobatoria():
    print("la nota minima necesaria pra aprobar el curso 6.0")
obtener_nota_minima_aprobatoria()

def calcular_promedio_ponderado(evaluacion, libreta):
    promedio = (evaluacion * 0.70) + (libreta * 0.30)
    return round(promedio, 1)
      
def generar_boleta(nombre_alumno, evaluacion, libreta):
    calificacion_final = calcular_promedio_ponderado(evaluacion, libreta)

    print(f"Alumno: {nombre_alumno}")
    print(f"Calificación final: {calificacion_final}")

    if calificacion_final == 10.0:
        print("Estado: Excelente")
        print("¿Necesita examen extraordinario?: No")
    elif calificacion_final == 7.0:
        print("Estado: Aprobado")
        print("¿Necesita examen extraordinario?: No")
    else:
        print("Estado: Reprobado")
        print("¿Necesita examen extraordinario?: Sí")


generar_boleta("Jessica", 70, 30)

  
import datetime

def saludar():
    print("Hola bienvenido")
saludar()

def mostrar_hora():
    hora_actual = datetime.datetime.now().strftime("%H ,%M ,%S ")
    print(f"la hora actual es: {hora_actual}")
mostrar_hora()

    #Now()consulta el reloj o la hora del SO
    #strftime convertir la fecha y la hora en texto, usando el formato establecido
    #f-string la letra f indica a python que procese el texto
    #e insertar las variables dentro de las llaves
    #{hora_actual} se toma el valor almacenado en la variable de hora_actual
    #y lo remplaza ahi mismo


#*/*/*/*/*/*/ EJEMPLOS /*/*/*/*/*/*/*

def recordatorio():
    print("No se te olvide hacer tarea")
recordatorio()       

def error_codigo():
    print(f"se a producido un error en el codigo vuelve a intentar mas tarde")
error_codigo()    

#Programa para Calificar una Nota
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario ingresar el valor de una nota para que èsta quede guardada como entero en la variable Nota
Nota = float(input('ingrese el valor de la nota, èsta va de 0 a 100: '))
#Se determina si la nota es aprobatoria o no al compararla con la mìnima aprobatoria que es 60.
#si la nota es menor a 60 el estudiante reprueba, caso contrario si la nota es mayor.
if (Nota>= 60):
    #Envía un mensaje por consola el cual indica que el estudiante aprobó
    print('El estudiante es Aprobado')
else:
    #Envía un mensaje por consola el cual indica que el estudiante reprobó
    print ('El estudiante es Reprobado')
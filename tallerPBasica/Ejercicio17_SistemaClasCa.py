#Sistema de calificaciones con bonificaciones
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
# se define la variable calificacion total en 0
CT = int(0)
#se le pide al usuario una calificacion
CaEs= int (input('ingrese la calificación (0-100): '))
#se le pide al usuario si hizo tareas adicionales
tareasAd= str(input('hizo tareas adicionales? (si o no)')).lower()
if (tareasAd == 'si'):
    #se define CT como la calificacion ingresada por el estudiante más el 5% de esta
    CT =CaEs*1.05
else:
    #se define calificacion total como la calificacion de entrada en caso tal de que el estudiante no haya hecho tareas adicionales
    CT=CaEs
#si la calificacion ingresada es mayor a 100, CT será definida como 100
if (CaEs>100 or CT > 100):
    CT = 100
#se imprime o muestra en consola la calificacion total
print (f"La calificacion final es: {CT}")
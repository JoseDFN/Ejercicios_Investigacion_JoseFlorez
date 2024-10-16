#Conversión de calificaciones numéricas a letras
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se le pide al usuario ingresar una calificacion del 0 al 100 y se guarda en la variable calificacion
Calificacion = int(input('ingrese una calificación (de 0 a 100):'))
#se define ClasificacionL como un string vacio
CalificacionL = str('')
#operacion match para clasificar la calificacion dada por el usuario (en numero) a una letra
match Calificacion:
    case Calificacion if 0<=Calificacion<=59:
        CalificacionL = 'F'
    case Calificacion if 60<=Calificacion<=69:
        CalificacionL = 'D'
    case Calificacion if 70<=Calificacion<=79:
        CalificacionL = 'C'
    case Calificacion if 80<=Calificacion<=89:
        CalificacionL = 'B'
    case Calificacion if 90<=Calificacion<=100:
        CalificacionL = 'A'
    case _:
        CalificacionL = 'No aceptable'
#se imprime en consola la calificacion en letra al usuario
print (f"Su calificación corresponde a: {CalificacionL}")
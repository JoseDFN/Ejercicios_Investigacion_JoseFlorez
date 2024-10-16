#Clasificación de edades
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario que digite la edad
EdadUsua = int(input('Ingrese la edad, si desea salir del programa digite un numero negativo: '))
#Mientras el usuario no ingrese un numero negativo el programa seguirá corriendo
while (EdadUsua >= 0):
#Se determina si el usuario es un niño y se el mensaje en consola
    if ((EdadUsua >=0) and (EdadUsua<=12)):
        print ('El usuario es un Niño')
#Se determina si el usuario es un adolescente y se da el mensaje en consola
    elif ((EdadUsua >= 13) and (EdadUsua <= 17)):
        print ('El usuario es un Adolescente')
#Se determina si el usario es un Adulto y se da el mensaje en consola
    elif ((EdadUsua >= 18) and (EdadUsua<=64)):
        print ('El usuario es un Adulto')
#Si ninguna de las condiciones de arriba se cumple, sale en consola que el usuario es un anciano
    else :
        print ('El usuario es un anciano')
    EdadUsua = int(input('Ingrese la edad y si quiere salir del programa digite un numero negativo: '))

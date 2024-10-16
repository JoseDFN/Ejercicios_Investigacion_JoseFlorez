#Clasificación de notas
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario que ingrese la nota
NotaUsua = int(input('Ingrese su nota (del 0 al 100): '))
#Se verifica si la nota es menor para clasificar como F
if (NotaUsua < 60):
    print ('Clasificado como F')
#Se verifica si la nota es mayor que el 60 y menor que el 69 para clasificar como D
elif (NotaUsua >= 60 and NotaUsua <= 69):
    print ('Clasificado como D')
#Se verifica si la nota es mayor a 70 y menor a 79 se clasifica como C
elif (NotaUsua >= 70 and NotaUsua <= 79):
    print ('Clasificado como C')
#Se verifica si la nota es mayor a 80 y menor a 89 para clasificarlo como B
elif (NotaUsua >= 80 and NotaUsua <=89 ):
    print ('Clasificado como B')
#Se verifica si la nota es mayor a 90 y menor a 100 para clasificarlo como A
elif (NotaUsua >= 90 and NotaUsua <=100):
    print ('Clasificado como A')
#Mostrarle al usuario que la nota ingresada no es valida
else:
    print('nota ingresada no valida')
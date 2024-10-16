#Números pares en un rango
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario que ingrese la variable minima del rango
NumMin=(int(input('Ingrese el numero mínimo para el rango: ')))
#se le pide al usuario que ingrese la variable maxima del rango
NumMax=(int(input('Ingrese el numero máximo para el rango: ')))
#bucle for en el que la variable i tomará valor de cada numero entre el rango min y max designado
for i in range (NumMin, (NumMax)+1):
    #parte logica que determina si el numero en i es par o si el numero es uno de los extremos del rango
    if (i%2 == 0 or i==NumMax or i == NumMin):
        #si el numero es par se imprime, o si el numero es uno de los extremos del rango
        print (i)

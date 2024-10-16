#Determinación del tipo de triángulo por angulo
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario que ingrese el valor de cada Angulo del triangulo
Angulo1=float(input('Ingrese el valor del primer angulo: '))
Angulo2=float(input('Ingrese el valor del segundo angulo: '))
Angulo3=float(input('Ingrese el valor del tercer angulo : '))
#Suma para determinar el total de los angulos internos del triangulo
sumT= (Angulo3+Angulo2+Angulo1)
#bucle que se encarga de hacer que las entradas de los angulos correspondan a los de un triangulo (suma de los angulos internos igual a 180°)
while (sumT!=180):
    print('Los angulos ingresados no corresponden a los de un triangulo (la suma de los angulos debe ser igual a 180°)')
    Angulo1=float(input('Ingrese el valor del primer angulo: '))
    Angulo2=float(input('Ingrese el valor del segundo angulo: '))
    Angulo3=float(input('Ingrese el valor del tercer angulo: '))
#Se compara la medida de los angulos del triangulo para determinar el tipo de éste y dar la salida determinada por consola
if ((Angulo1<90) and (Angulo2<90) and (Angulo3<90)):
    print('El triangulo indicado es agudo ')
elif ((Angulo1==90) or (Angulo2 == 90) or (Angulo3 == 90)):
    print('El triangulo indicado es rectángulo')
elif((Angulo1 > 90) or (Angulo2 > 90) or (Angulo3 > 90)):
    print('El triangulo es obtuso')
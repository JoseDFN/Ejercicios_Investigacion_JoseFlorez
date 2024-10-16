#Cálculo del tiempo de viaje
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se le pide al usuario la distancia total en Km
Distancia = int (input('Ingrese la distancia a recorrer en Km: '))
#se le pide al usuario la velocidad promedio en Km/H
VelProm = int (input('Ingrese la velocidad promedio en Km/H: '))
#calculo tiempo total
TT = Distancia/VelProm
#mensaje consola tiempo total
print (f"El tiempo total es de: {TT:.2f}h")
#mensaje de advertencia si va a más de 120km/h
if (VelProm> 120):
    print ('Precaución, vas muy rapido💨💨💨')
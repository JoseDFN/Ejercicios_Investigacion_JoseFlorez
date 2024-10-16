#Comparación de tres números
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario ingresar 3 numeros
N1 = float(input('Ingrese el primer Numero: '))
N2 = float(input('Ingrese el segundo Numero: '))
N3 = float(input('Ingrese el tercer Numero: '))
#Se comparan los numeros para determinar el mayor
if (N1> N2 and N1 > N3):
    print (f"el numero mayor es {N1}")
elif (N2 > N1 and N2 > N3):
    print (f"el numero mayor es {N3}")
elif(N3 > N1 and N3 > N2):
    print (f"el numero mayor es {N3}")
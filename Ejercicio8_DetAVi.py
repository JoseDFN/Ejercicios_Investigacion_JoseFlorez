#Determinación de año bisiesto
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario ingresar el año
AñoUsuario = int(input('Ingrese el numero del año: '))
#Se evalua si el año es divisible en 4 y 400, pero no entre 100. así determinando si es bisiesto o no y luego mostrando en consola el mensaje
if (((AñoUsuario % 4) == 0) and ((AñoUsuario % 100) != 0) or ((AñoUsuario % 400)==0)):
    print('El año es bisiesto')
else : 
    print ('El año no es bisiesto')
#Número positivo, negativo o cero
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario que ingrese un numero
NumUsuario = float(input('Ingrese un numero: '))
#Se evalua si el numero es negativo
if (NumUsuario<0):
    print ('El numero ingresado es Negativo')
#Se evalua si el numero es positivo
elif (NumUsuario>0):
    print ('El numero ingresado es Positivo')
#Se evalua si el numero es 0
elif (NumUsuario == 0):
    print ('El numero ingresado es igual a 0')
#Opcion por si el numero es diferente de los de arriba
else:
    print('El numero ingresado por el usuario no es real 😖')
#Programa para verificar si un numero es par o impar
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario ingresar un nùmero para que èsta quede guardada como entero en la variable Numero
Numero = int(input('Ingrese el numero a verificar si es par o impar: '))
#Se evalua el numero mediante la operacion modulo para determinar si al dividir entre 2 el numero tiene un residuo.
#En caso tal de que se tenga residuo, el numero serìa impar y, en caso tal de que no lo tenga serìa par
if (Numero%2==0):
    #se manda un mensaje en consola en el que se agrega el numero que ingreso el usuario y que es par
    print(f"El numero {Numero} es Par")
else:
    #se manda un mensaje en consola en el que se agrega el numero que ingreso el usuario y que es impar
    print(f"El numero {Numero} es Impar")
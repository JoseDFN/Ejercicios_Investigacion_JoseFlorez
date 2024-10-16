#Adivina el número (con while )
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se inicia la variable Suma de pares (SumPars) como entero y en 0
SumPars = int(0)
#se le pide al usuario que ingrese un numero y se le da la instruccion de que ingrese un numero primo para finalizar el programa
NumeroUsua = int (input('Ingrese un numero para sumar, si desea finalizar el programa ingrese un numero primo: '))
#bucle que se ejecuta mientras el numero ingresado por el usuario sea par
while (((NumeroUsua%2)==0)):
    #se suma el numero ingresado a la variable SumPars
    SumPars += NumeroUsua
    #se le pide al usuario que ingrese otro numero
    NumeroUsua = int(input('Ingrese otro numero: '))
#al finalizar el bucle se imprime en consola la sumatoria de los numeros, contenida en la variable SumPars.
print (f"La sumatoria de los numeros pares es: {SumPars}")
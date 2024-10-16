#Factorial de un número
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se inicializa la variable factorial en 1
Factorial = int(1)
#Se le pide al usuario que ingrese un numero
NumeroUsuario = int(input('Ingrese un numero: '))
#se establece un loop con una variable i de control para que ésta "llegue" al valor de la variable NumeroUsuario
for i in range (1, NumeroUsuario +1):
    #Se multiplica la variable Factorial con el valor de i
    Factorial *= i
#Se da el resultado del factorial para el numero ingresado
print (f"El factorial del numero {NumeroUsuario} es: {Factorial}")
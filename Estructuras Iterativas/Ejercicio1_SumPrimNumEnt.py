#Suma de los primeros N números enteros
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se inicializa la variable i como un entero en 0
i=int(0)
#se inicializa la variable Sumatoria Total (STot) como un entero en 0
STot=int(0)
#se le pide al usuario que ingrese el valor
NumUsuario = int(input('Ingrese un numero: '))
#se inicia el bucle con la variable i y luego se establece el bucle para que se llegue al numero de la variable NumUsuario
for i in range (1, NumUsuario +1):
    #Se se le suma a STot la variable i
    STot+=i
#se muestra por consola la suma total de los primeros n numeros enteros
print(f"la suma total de los primeros n numeros enteros es: {STot}")

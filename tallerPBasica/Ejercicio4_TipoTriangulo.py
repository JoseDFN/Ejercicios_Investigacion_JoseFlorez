#Determinación del tipo de triángulo
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario que ingrese el valor de cada lado del triangulo
Lado1=float(input('Ingrese el valor del primer lado del triangulo: '))
Lado2=float(input('Ingrese el valor del segundo lado del triangulo: '))
Lado3=float(input('Ingrese el valor del tercer lado del triangulo: '))
#Se compara la medida de los lados para determinar el tipo de éste
if (Lado1==Lado2==Lado3):
    print('El triangulo indicado es equilatero ')
elif (Lado1==Lado2 or Lado1==Lado3 or Lado2==Lado3):
    print('El triangulo indicado es isóceles')
else:
    print('El triangulo es escaleno')
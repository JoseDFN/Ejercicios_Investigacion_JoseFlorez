#Contador de vocales en una cadena
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se inicializa la variable contador de Vocales totales(VTot) en 0 y como entero
VTot=int(0)
#se establece el string con las vocales dentro de la variable Vocales
Vocales = str ('aeiou')
#se le pide una palabra al usuario
Palabra = str(input('Ingrese una palabra: '))
#se hace un bucle en el que se le va asignando cada letra de la palabra ingresada por el usuario a la variable i
for i in Palabra:
    #se compara la letra designada de la palabra con las vocales contenidas en la varaible Vocales
    if i in Vocales:
        #si la letra coincide se le suma 1 a la variable VTot
        VTot+=1
#Se muestra por consola la cantidad de vocales en la palabra ingresada
print(f"El total de vocales en la palabra {Palabra} son: {VTot}")
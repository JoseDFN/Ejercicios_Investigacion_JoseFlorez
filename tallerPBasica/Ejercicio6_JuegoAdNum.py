#Juego de adivinanza de números
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se importa el modulo random
import random
#Se le pide al usuario que ingrese un numero del 1 al 10
NumUsuario = int(input('Ingrese un numero del 1 al 10: '))
#se define el rango de los numeros a adivinar
Aleatorio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#se define el inicio de la lista a adivinar
inicio = 1
#se define el fin de la lista
fin = 10
#se definen los pasos o saltos
paso = 1
#se hace uso de la funcion random.randrange(inicio, fin, paso) para que guarde un numero entero dentro de la lista seleccionada en la variable NumAleatorio
NumAleatorio = random.randrange(inicio, fin, paso)
#se hace un bucle para que mientras el usuario no haya adivinado el numero, éste pueda seguir intentandolo
while (NumUsuario != NumAleatorio):
    #mensaje de volver a intentar
    NumUsuario = int(input('Sigue intentando😵: '))
#mensaje de victoria en el que se revela el numero aleatorio
print (f"🎆🎆🎆Felicitaciones, lo conseguiste, el numero era {NumAleatorio}🎆🎆🎆")
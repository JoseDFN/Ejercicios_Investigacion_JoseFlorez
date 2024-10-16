#Adivina el número (con while )
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se importa el modulo random
import random
#se establece el numero secreto al seleccionar aleatoriamente uno desde 1 hasta 100
NumSecret = (random.randint(1, 100))
#Se le pide al usuario que ingrese un numero
NumUsuario = int(input('Ingresa el numero y prueba tu suerte: '))
#mientras que el numero ingresado por el usuario no sea igual al numero secreto el bucle le seguirá pidiendo un numero al usuario y dandole pistas
while (NumUsuario != NumSecret):
    #si el numero secreto es mayo, le programa le dirá al usuario que siga intentando y que el numero que busca es algo mayor
    if (NumSecret > NumUsuario):
        NumUsuario = int(input('sigue intentando, el numero que estas buscando es algo mayor 🙃: '))
    #por el contrario, si el numero secreto es menor, le dira al usuario que siga intentando y que el numero que busca es algo menor
    else:
        NumUsuario = int(input('sigue intentando, el numero que estas buscando es algo menor 🙃: '))
#mensaje de celebración por haber encontrado el numero correcto
print (f"🎆🎆🎆Felicitaciones, lo conseguiste, el numero era {NumSecret}🎆🎆🎆")
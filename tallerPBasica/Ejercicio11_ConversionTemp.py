#Clasificación de edades
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario ingresar una temperatura
TempUsu = float(input('Ingrese la temperatura a convertir: '))
#se le pide al usuario ingresar la escala
Escala = str(input('Ingrese el tipo de escala  (C o F): ')).upper()
match Escala:
    case 'C':
        #se calcula de grados C° a F°
        Fahrenheit = ((TempUsu * 1.8) + 32)
        print (f"La temperatura es {Fahrenheit} grados Fahrenheit")
    case 'F':
        #Se calcula de grados F° a C°
        Celsius = ((TempUsu - 32) / 1.8)
        print (f"La temperatura es {Celsius} grados celsius")
    case _:
        #Caso para cuando la escala no es la indicada
        print ('La escala no es aceptada')
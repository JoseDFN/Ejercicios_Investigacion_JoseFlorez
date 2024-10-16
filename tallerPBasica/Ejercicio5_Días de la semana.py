#Días de la semana usando match
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario que ingrese un numero del 1 al 7 para dar como respuesta el día de la semana
Diausuario = int(input('Ingrese, de 1 a 7, un día de la semana: '))
#el condicional match da la respuesta con el día de la semana determinado a partir de la entrada del usuario
match (Diausuario):
    #Caso para el día 1 (Lunes)
    case 1:
        print (f"El día {Diausuario} de la semana es Lunes 😃")
    #Caso para el día 2 (Martes)
    case 2:
        print (f"El día {Diausuario} de la semana es Martes 😃")
    #Caso para el día 3 (Miercoles)
    case 3:
        print (f"El día {Diausuario} de la semana es Miercoles 😃")
    #Caso para el día 4 (Jueves)
    case 4:
        print (f"El día {Diausuario} de la semana es Jueves 😃")
    #Caso para el día 5 (Viernes)
    case 5:
        print (f"El día {Diausuario} de la semana es Viernes 😃")
    #Caso para el día 6 (Sabado)
    case 6:
        print (f"El día {Diausuario} de la semana es Sabado 😃")
    #Caso para el día 7 (Domingo)
    case 7:
        print (f"El día {Diausuario} de la semana es Domingo 😃")
    #Caso para una entrada diferente a los días del 1 al 7
    case _:
        print ('La entrada o día agregado no corresponde a ningun día de la semana.')
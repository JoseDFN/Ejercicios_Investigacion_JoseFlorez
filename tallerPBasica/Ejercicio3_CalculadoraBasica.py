#Calculadora bàsica (+, -, *, /)
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se define la variable Acalculadora como iniciador para que èsta estè activa
Acalculadora = True
#Se definen la variable opciones con las opciones determinadas
OpcionesC = '+. Suma\n-.Resta\n*. Multiplicaciòn\n/. Divisiòn\n0. Salir'
OpcionSelectU = ''
Respuesta = float(0)
while (Acalculadora):
    input('De enter para continuar')
    Numero1 = float(input("Ingrese el valor del primer numero: "))
    Numero2 = float(input("Ingrese el valor del segundo numero (Denominador en caso de division): "))
    print(f'ingrese la opcion de la operaciòn a realizar (+, -, *, /) y, en caso de que quiera terminar la tarea del programa, ingrese "0": ', end="")
    OpcionSelectU = input('')
    match(OpcionSelectU):
        #Caso para suma
        case '+':
            Respuesta = Numero1+Numero2
            print(f"la suma de los numeros {Numero1} y {Numero2} es: {Respuesta}")
        #Caso para resta
        case '-':
            Respuesta = Numero1-Numero2
            print(f"la resta de los numeros {Numero1} y {Numero2} es: {Respuesta}")
        #Caso para multiplicación
        case '*':
            Respuesta = Numero1*Numero2
            print(f"la multiplicacion de los numeros {Numero1} y {Numero2} es: {Respuesta}")
        #Caso para división
        case '/':
            #seccion logica en caso tal de que el numero del denominador ingresado sea 0
            if (Numero2!=0):
                Respuesta = Numero1/Numero2
                print(f"la division de los numeros {Numero1} y {Numero2} es: {Respuesta}")
            else:
                print('No se puede dividir entre 0')
        #Caso para terminar el proceso de la calculadora
        case '0':
            Acalculadora = False
        #Caso que se usa cuando el usuario da otra entrada diferente a las aceptadas
        case _:
            print('ingresò una operacion que no se encuentra en esta version de la calculadora')
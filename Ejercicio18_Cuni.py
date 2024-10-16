#Sistema de evaluación de créditos universitarios
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se le pide al usuario que ingrese el numero de materias cursadas
NMaterias = int (input('Ingrese el numero de materias que ha cursado: '))
#contador para creditos
credMat = int(0)
#variable control para el bucle
i = int(0)
#bucle while con variable de control para el numero de materias cursadas dado por el usuario
while (i<NMaterias):
    #se le pide al usuario ingresar el valor de las calificaciones de las materias cursadas para ser guardado en la variable NotaM
    NotaM = int (input('ingrese la calificacion de la materia (0-100): '))
    #se verifica si la nota es mayor o igual a 60 para dar 3 creditos por cada una
    if (NotaM>= 60):
        credMat +=3
    #aumento en 1 de la variable control para el ciclo
    i+=1
#se muestra en consola la cantidad total de creditos obtenidos
print(f"El total de creditos obtenidos es de: {credMat}")
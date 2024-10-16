#Sistema de estacionamiento con tarifas progresivas
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#se definen las variables de costo y horas finales, para el funcionamiento del problema, en 0
Hfin = int (0)
Ctot = int (0)
#Se le pide al usuario la cantidad de horas de parqueo para guardarlas en la variable HParqueo
HParqueo = int(input('Ingrese las horas de parqueo: '))
#se evalua si las horas de parqueo son mayores a 1, se les resta 1 y luego se agrega a la variable de costo total (Ctot) 5
if (1<=HParqueo>0):
    HParqueo-=1
    Ctot= 1*5
#se evalua si, luego de haberle restado 1 a la variable horas de parqueo, ésta sigue teniendo un valor. si lo tiene, se guarda las horas totales a contar para el pago
#al definirla como: hora final es igual a horas de parqueo menos las horas de parqueo menos 3, así se puede determinar la cantidad de horas a contar
if (1<=HParqueo):
    if (1<=HParqueo<=3):
        Ctot += (HParqueo*4)
        HParqueo-=HParqueo
    elif(HParqueo>=4):
        Hfin =(HParqueo-(HParqueo-3))
        #con las horas "contables", se saca el valor total a agregar a la variable Ctot multiplicando las horas "contables" por 4
        Ctot += (Hfin*4)
        #se le resta 3 a las horas de parqueo "restantes"
        HParqueo-=3
#si quedan horas "restantes", estas se multiplicaran por 3 y el resultado sera agregado a la variable Ctot
if(HParqueo>=1):
    Ctot+=(HParqueo*3)
#se le da al usuario la cantidad a pagar por las horas de parqueo
print (f"Debe pagar {Ctot}$ por las horas de parqueo")
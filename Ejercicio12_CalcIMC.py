#Calculadora de IMC (Índice de Masa Corporal)
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario ingresar su peso en Kg
Peso = float(input('Ingrese su peso en Kg: '))
#Se le pide al usuario ingresar su altura en metros
Altura = float(input('Ingrese su altura en Metros: '))
#Se calcula el indice de masa corporal
IMC = float (Peso / (Altura ** 2))
#Se determina si esta delgado, normal, con sobre peso y/o obeso
if (IMC < 18.5):
    print ('Uds esta delgado')
elif ((IMC >= 18.5) and (IMC <= 24.9)):
    print ('Su peso esta Normal')
elif ((IMC >= 25) and (IMC <= 29.9)):
    print('Uds esta con sobre peso')
else:
    print ('uds esta con obesidad')
print (f"Su IMC es de {IMC}")
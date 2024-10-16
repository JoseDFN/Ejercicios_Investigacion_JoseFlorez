#Cálculo del salario neto
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se le pide al usuario ingresar el pais
Pais = str (input('ingrese su país (colombia, peru, ecuador): ')).strip() .lower()
#se le pide al usuario ingresar el salario
Salario = int (input('Ingrese su salario: '))
#se saca el salario total
match Pais:
    case 'colombia':
        St = Salario*0.8
    case 'peru':
        St = Salario*0.85
    case 'ecuador':
        St = Salario*0.9
    case _:
        St = Salario*0.75
#se le muestra al usuario el salario total despues de impuestos
print (f"El salario total despues de impuestos dependiendo del país es: {St}")
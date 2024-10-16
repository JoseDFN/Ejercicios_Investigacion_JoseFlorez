#Adivinanza de letras
#Creaciòn 13 de Septiembre
#Josè David Flòrez Navarrete
#Grupo J1 apolo11
#Se define la letra secreta
letraS = "A"
#se le pide al usuario que ingrese la letra para adivinar
letraU = input("Adivina la letra secreta: ").upper()
Active = True
while (Active):
    #se determina si el usuario adivino la letra o no
    match letraU:
        case 'A':
            print (f"🎆🎆🎆Felicitaciones, lo conseguiste, la letra era {letraS}🎆🎆🎆")
            Active = False
        case _:
              letraU = input("Adivina la letra secreta: ").upper()
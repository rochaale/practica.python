##Escribe un programa que solicite al usuario su año de nacimiento y muestre en qué
##año cumplirá 18, 21 y 100 años.
lista_años = [18, 21, 100]
año_nacimiento = int(input ("Ingresa el año de tu nacimeinto: "))
for edad in lista_años:
    año = año_nacimiento + edad
    print(f"Usted cumplira {edad} en el año: {año}")
    

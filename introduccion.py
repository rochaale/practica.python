##Escribe un programa que solicite al usuario su año de nacimiento y muestre en qué
##año cumplirá 18, 21 y 100 años.
lista_años = [18, 21, 100]
año_nacimiento = int(input ("Ingresa el año de tu nacimeinto: "))
for edad in lista_años:
    año = año_nacimiento + edad
    print(f"Usted cumplira {edad} en el año: {año}")
    
##Escribe un programa que solicite al usuario una cantidad de segundos y muestre
##cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
##hora, 1 minuto y 1 segundo.
seg = int(input("Introduzca una cantidad de segundos: "))
hora = seg // 3600
resto = seg % 3600
minutos = resto // 60
resto = resto % 60
segundos = resto 
print(f"Cantidad de horas {hora} , cantidad se minutos {minutos}, cantidad de segundos {segundos}")

#Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
#del 1 al 10 utilizando un bucle for.
numero = int(input("Ingrese un numero: "))
for i in range(1,11):
    mult = i * numero
    print(f"{numero} x {i} = {mult}")

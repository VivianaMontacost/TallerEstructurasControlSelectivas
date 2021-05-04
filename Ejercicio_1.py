""""
Entradas
valorinversion int inversion
interesmensual float interes
salidas
totalinteres str tipo
total float str tipo
"""
inversion = int (input ("Ingrese la cantidad de dinero a invertir: "))
interes = float (input ("Ingrese qué porcentaje de interés mensual pagará el banco: "))
totalinteres=(inversion*interes)
total=(inversion+totalinteres)
if (totalinteres>100000):
  print ("Sí vale la pena reinvertir ")
  print (("El total de dinero en su cuenta será de:"),(total))
else:
  print ("No Vale la pena reinvertir")



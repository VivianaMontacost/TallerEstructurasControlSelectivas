""""
Entradas
Salario float S
Salidas
SalarioFinal15 float salario15
SalarioFinal12 float salario12
"""
S = float (input ("Ingrese el valor de su salario mensual:"))
aumento15=(S*0.15)
salario15=(S+aumento15)
aumento12=(S*0.12)
salario12=(S+aumento12)
if (S < 900000):
  print ("Su salario tiene un 15% de aumento")
  print (("Su salario total será de: "),(salario15))
if (S > 900000):
  print ("Su salario tiene un 12% de aumento")
  print (("Su salario total será de: "),(salario12))
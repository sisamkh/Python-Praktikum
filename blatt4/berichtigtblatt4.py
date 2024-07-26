import numpy as np
import math as math


def funktion_von_x(f,x):
   return f(x)

def funktion(n):
   return  np.exp(n**2)                #Hier Funktion einsetzen

a = 0
b = 1
m = 4

def trapezregel(f,a,b,m):
    
   h = (b-a)/m
   mittleresTrapez = 0
   for i in range(1,m):
      mittleresTrapez += funktion_von_x(f,a+i*h)

   mittleresTrapez *= 2

   trapez = 1/8*(funktion_von_x(f,a) + mittleresTrapez + funktion_von_x(f,b))
   return trapez

def simpsonregel(f,a,b,m):

   h = (b-a)/6*m
   mittlererWert = 0
   for i in range(1,2*m):
      if i % 2 == 0:
         mittlererWert += 2*funktion_von_x(f,a+i*(h/2*m))
      else:
         mittlererWert += 4*funktion_von_x(f,a+i*(h/2*m))
   
   simpson = h*(funktion_von_x(f,a)+mittlererWert+funktion_von_x(f,b))
   return simpson

def gauss_legendre2(f,a,b):
   t1 = 0.5 * (b - a) * 1/math.sqrt(3) + 0.5 * (b + a)      #Transformation von [-1,1] auf [a,b]
   t2 = 0.5 * (b - a) * (-1/math.sqrt(3)) + 0.5 * (b + a)
   integral = (b-a)/2*(funktion_von_x(f,(b-a)/2*t1+(b+a)/2)+funktion_von_x(f,(b-a)/2*t2+(b+a)/2)) #festgelegte Werte für n=2(s. Wikipedia)
   return integral

def gauss_legendre3(f,a,b):
   t1 = 0.5 * (b - a) * 0 + 0.5 * (b + a)      #Transformation von [-1,1] auf [a,b]
   t2 = 0.5 * (b - a) * math.sqrt(3/5) + 0.5 * (b + a)
   t3 = 0.5 * (b - a) * (-1)*math.sqrt(3/5) + 0.5 * (b + a)

   integral = (b-a)/2*(8/9 * funktion_von_x(f,(b-a)/2*t1+(b+a)/2)+5/9 * funktion_von_x(f,(b-a)/2*t2+(b+a)/2)+5/9 * funktion_von_x(f,(b-a)/2*t3+(b+a)/2))
   return integral #festgelegte Werte für n=3(s. Wikipedia)


print("trapez: ", trapezregel(funktion,0,1,4))
print("simpson: ", simpsonregel(funktion,0,1,4))
print("gauss2: ", gauss_legendre2(funktion,0,1))
print("gauss3: ", gauss_legendre3(funktion,0,1))

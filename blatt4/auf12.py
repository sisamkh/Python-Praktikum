# Gruppe 3
# Sisam Khanal
# Eya Rouissi
# Vladimir Suschevici

import numpy as np
import math as math
import matplotlib.pyplot as plt

def trapezregel(f,a,b,m):

   h = (b-a)/m
   mittleresTrapez = 0
   for i in range(1,m):
      mittleresTrapez += f(a+i*h)

   mittleresTrapez *= 2

   trapez = h/2 * (f(a) + mittleresTrapez + f(b))
   return trapez

def simpsonregel(f, a, b, m):
    if m % 2 == 1:
        raise ValueError("m muss gerade sein für die Simpson-Regel.")
    h = (b - a) / m
    sum = f(a) + f(b)
    for i in range(1,m):
        x = a + i*h
        sum += 4 * f(x) if i % 2 != 0 else 2 * f(x)
    return (h / 3) * sum

def gauss_legendre2(f,a,b):
   t1 = 0.5 * (b - a) * 1/math.sqrt(3) + 0.5 * (b + a)      #Transformation von [-1,1] auf [a,b]
   t2 = 0.5 * (b - a) * (-1/math.sqrt(3)) + 0.5 * (b + a)
   integral = (b-a)/2*(f((b-a)/2*t1+(b+a)/2)+f((b-a)/2*t2+(b+a)/2)) #festgelegte Werte für n=2(s. Wikipedia)
   return integral

def gauss_legendre3(f,a,b):
   x1, x2, x3 = 0, -np.sqrt(3/5), np.sqrt(3/5)
   t1 = 0.5 * (b - a) * x1 + 0.5 * (b + a)
   t2 = 0.5 * (b - a) * x2 + 0.5 * (b + a)
   t3 = 0.5 * (b - a) * x3 + 0.5 * (b + a)

   w1 = 5/9
   w2 = 8/9
   w3 = 5/9

   return (b - a) / 2 * (w1 * f(t1) + w2 * f(t2) + w3 * f(t3)) #festgelegte Werte für n=3


def f(x):
    return x**3 * np.sin(x)

a,b = -np.pi/2, np.pi/2
exakte_integral = 3/2 * (np.pi ** 2 - 8)

fehler_trapezoidal = []
fehler_simpson = []
fehler_gauss2 = []
fehler_gauss3 = []

arr =  [2**k for k in range(1, 11)]

for m in arr:
    I_trap = trapezregel(f, a, b, m)
    I_simp = simpsonregel(f, a, b, m)
    I_gauss2 = gauss_legendre2(f, a, b)
    I_gauss3 = gauss_legendre3(f, a, b)

    fehler_trapezoidal.append(abs(exakte_integral - I_trap))
    fehler_simpson.append(abs(exakte_integral - I_simp))
    fehler_gauss2.append(abs(exakte_integral - I_gauss2))
    fehler_gauss3.append(abs(exakte_integral - I_gauss3))

# Plotten
plt.figure(figsize=(10, 6))
plt.loglog(arr, fehler_trapezoidal, label='Trapezregel')
plt.loglog(arr, fehler_simpson, label='Simpsonregel')
plt.loglog(arr, fehler_gauss2, label='Gauß-Legendre (n=2)')
plt.loglog(arr, fehler_gauss3, label='Gauß-Legendre (n=3)')
plt.xlabel('m (Anzahl der Unterteilungen)')
plt.ylabel('Absolute Fehler |I - I~|')
plt.title('Logarithmische Darstellung der Integrationsfehler')
plt.legend()
plt.grid(True)
plt.show()

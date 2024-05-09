# Aufgabe 3 Blatt 1
# Gruppe 3
# Eya Rouissi(1913192)
# Sisam Khanal (2312802)
# Vladimir Suschevici(1732301)

import math

def fnk(x):
    if x<0 :
        print("x soll größer null sein ")
        return 0
    y=(math.exp(x)-1)/x
    return y

for k in range(1,21): # von 1 zu 20
    print(fnk(pow(10,-k)))
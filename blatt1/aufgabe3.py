# Gruppe 3
# Sisam Khanal
# Eya Rouissi
# Vladimir Suschevici

import math

def fnk(x):
    if x<0 :
        print("x soll größer null sein ")
        return 0
    y=(math.exp(x)-1)/x
    return y

for k in range(1,21): # von 1 zu 20
    print(fnk(pow(10,-k)))

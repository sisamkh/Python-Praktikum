# Gruppe 3
# Sisam Khanal
# Eya Rouissi
# Vladimir Suschevici

import time
import random

def polym_auswertung(x, koef):
    summe = 0
    for i in range(len(koef)):
        summe += koef[i]*(x ** i)
    return summe

def horner_schema(x,koef):
    auswertung = 0
    for i in range(len(koef)-1, -1,-1): # Läuft von len(koef)-1 zu 0
        auswertung = auswertung*x + koef[i]
    return auswertung

# erzeugt eine liste mit k beliebige element.
def rand_list(k):
    randomlist = []
    for i in range(k):
        n = random.randint(1,100000)
        randomlist.append(n)
    return randomlist

r_ll = rand_list(20)


start = time.time()
print(polym_auswertung(70,r_ll))
end = time.time()
print("Auswertung der Polynomfunktion: ",end-start)


start = time.time()
print(horner_schema(70,r_ll))
end = time.time()
print("Auswertung mit Horner-Schema: ",end-start)

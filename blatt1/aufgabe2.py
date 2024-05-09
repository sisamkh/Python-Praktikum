# Aufgabe 2 Blatt 1
# Gruppe 3
# Eya Rouissi(1913192)
# Sisam Khanal (2312802) 
# Vladimir Suschevici(1732301)

import math as m

# n-te Näherung
def limit_approx(n):
    return (1+1/n) ** n

# n = 10^1 ... 10^20 Näherungen
def limit_approx_20():
    for i in range(1,21):
        p = 10 ** i
        print(f"10^{i}.te Näherungen mit Limus ist: ", limit_approx(p))
limit_approx_20()


def kte_partialsumme(k):
    sum = 0
    for i in range(k):
        sum += 1/m.factorial(i)
    return(sum)

print(kte_partialsumme(90))

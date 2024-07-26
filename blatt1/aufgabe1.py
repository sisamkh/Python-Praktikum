# Gruppe 3
# Sisam Khanal
# Eya Rouissi
# Vladimir Suschevici


def maschinengenaueigkeit(n):
    ep = 1/3
    wert = 3
    for i in range(n):
        ep = ep * 1/3
        wert = wert * 3
    return ep, 1/wert

# Berechnung und Ausgabe der Maschinengenauigkeit
genauigkeit = maschinengenaueigkeit(29)
print("Die experimentell bestimmte Maschinengenauigkeit ε0 beträgt:", genauigkeit)

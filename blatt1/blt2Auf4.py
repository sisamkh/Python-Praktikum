import math

def funk(x):
    return - pow(math.sin(x), 2)/ pow(x,2)

for i in range(1,13):
    print(f"Für 10^-{i}: ", funk(pow(10,-i)))
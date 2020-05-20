import math

f = float(input())

if f - math.floor(f) >= 0.5:
    print(math.ceil(f))
else:
    print(math.floor(f))

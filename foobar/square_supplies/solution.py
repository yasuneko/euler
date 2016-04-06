import math

def answer(n):
    count = 0
    while n > 0:
        x = int(math.floor(math.sqrt(n)))
        n = n - (x ** 2)
        count += 1
    return

answer(24)

answer(160)

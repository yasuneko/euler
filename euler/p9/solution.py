from math import factorial
import sys

sys.path.append('../../utils')

from override_utils import *

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

value = 5
count = 0

def nCr(n,r):
    return factorial(n)/ (factorial(r) * factorial(n - r))

stuffa = []
stuffb = []
stuffc = []

for a in range(nCr(value - 1, 2)):
    stuffa.extend([[a + 1]] * (value - a - 2))

print stuffa

for b in range(1, value):
    stuffb.extend([[b + 1]] * (value - b - 1))

print stuffb

for c in range(2, value):
    stuffc.extend([[c + 1]] * (c - 1))

print stuffc

for i in range(len(stuffa)):
    print stuffa[i], stuffb[i], stuffc[i]
exit()

for a in inclusive_range(1, value):
    for b in range(a, value - a):
        for c in range(b, value - a - b):
            stuff.append([a, b, c])
exit()

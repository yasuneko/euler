from math import sqrt
import sys

sys.path.append('../utils')

from prime_utils import is_prime

"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
value = 600851475143
#value = 25
#value = 13195

small_factor = 1
large_factor = value

factors = []

while small_factor < large_factor:
	if value % small_factor == 0:
		large_factor = int(value / small_factor)
		factors.append(large_factor)
		factors.append(small_factor)
	small_factor += 1

for factor in sorted(factors, reverse=True):
	if is_prime(factor):
		print factor
		break

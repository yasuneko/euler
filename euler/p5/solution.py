from collections import Counter
from math import ceil, sqrt
from sets import Set
import sys

sys.path.append('../../utils')

from override_utils import *
from prime_utils import is_prime

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

max_divisor = 20
#max_divisor = 10

def get_prime_factors(val):
	prime_factors = []
	d = val
	factor = 2
	while factor <= d:
		if is_prime(factor):
			while d % factor == 0:
				d //= factor
				prime_factors.append(factor)
		factor += 1
	return sorted(prime_factors)

prime_factors = []
for i in inclusive_range(2, max_divisor):
	divisor_prime_factors = get_prime_factors(i)
	if not prime_factors:
		prime_factors = divisor_prime_factors
	else:
		prime_factors.extend(list((Counter(divisor_prime_factors)-Counter(prime_factors)).elements()))

print reduce(lambda x, y: x*y, prime_factors)

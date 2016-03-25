from math import sqrt

"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
value = 600851475143
#value = 25
#value = 13195

def is_prime(val):
	if val == 1:
		return False
	elif val in (2,5):
		return True
	elif not val%10 in (0,2,4,5,6,8):
		prime = True
		for i in range(2,int(sqrt(val))):
			if val%i == 0:
				prime = False
		return prime
	return False

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

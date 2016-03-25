from math import sqrt
import unittest

from override_utils import *

def is_prime(val):
	if val == 1:
		return False
	elif val in (2,5):
		return True
	elif not val%10 in (0,2,4,5,6,8):
		prime = True
		for i in inclusive_range(2,int(sqrt(val))):
			if val%i == 0:
				prime = False
		return prime
	return False

if __name__ == '__main__':
	class Test(unittest.TestCase):
		def test_is_prime(self):
			self.assertFalse(is_prime(1))
			self.assertTrue(is_prime(2))
			self.assertTrue(is_prime(3))
			self.assertFalse(is_prime(4))
			self.assertTrue(is_prime(19))
			self.assertFalse(is_prime(21))

	unittest.main()

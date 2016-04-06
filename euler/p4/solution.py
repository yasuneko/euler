#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

smallest = 100 * 100
largest = 999 * 999

x = range(100, 999)

all = Set()

for y in range(100,999):
	all.update([x1 * y for x1 in x])

def check_palindrome(val):
	val_str = str(val)
	val_len = len(val_str)
	
	if val_str == val_str[::-1]:
		return True
	else:
		return False

for i in sorted(all, reverse=True):
	if check_palindrome(i):
		print i
		break


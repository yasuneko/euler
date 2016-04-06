#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../../utils')

from prime_utils import is_prime

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

count = 0
max_count = 10001
num = 2

while count < max_count:
    if is_prime(num):
        count += 1
        if count == max_count:
            print num
    num += 1

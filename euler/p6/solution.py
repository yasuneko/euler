#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../../utils')

from override_utils import *

"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

value = 100

number_list = inclusive_range(value)

def square(x):
    return x*x

print square(sum(number_list)) - sum(map(square, number_list))

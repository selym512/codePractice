#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

output = ""

for x in range(m):
    for y in range(n):
        output += matrix[y][x]
        
output = re.sub(r'\b\W+\b', ' ', output, 0)
print(output)
        

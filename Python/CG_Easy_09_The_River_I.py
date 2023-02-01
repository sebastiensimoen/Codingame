import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def sum_val (nb):
    sum = 0
    while nb:
        sum += nb % 10
        nb = nb // 10
    return sum

r_1 = int(input())
r_2 = int(input())

while r_1 != r_2:
    if r_1 > r_2:
        r_2 = r_2 + sum_val(r_2)
    else:
        r_1 = r_1 + sum_val(r_1)
        
# Write an answer using print
print(r_1)

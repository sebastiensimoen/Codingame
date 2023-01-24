import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

j=0
t_0 = 0

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if j==0:
        t_0 = t
    if abs(t) < abs(t_0):
        t_0 = t
    if abs(t) == abs(t_0) and t > t_0:
        t_0 = t

    j = j+1

# Write an answer using print
print(t_0)

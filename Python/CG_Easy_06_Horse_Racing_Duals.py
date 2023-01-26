import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

horse_list = []

n = int(input())
for i in range(n):
    pi = int(input())
    horse_list.append(pi)

horse_list.sort()
min_diff = min(horse_list[i] - horse_list[i-1] for i in range(1, n))

# Write an answer using print
print(min_diff)

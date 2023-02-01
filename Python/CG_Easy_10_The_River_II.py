import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def nextValue (nb):
    numbers = str(nb)
    numbers = [int(x) for x in numbers]
    return nb  + sum(numbers)

r_1 = int(input())
output = "NO"

for i in range(r_1, 1, -1):
    r_2 = nextValue(i)
    if r_2 == r_1:
        output = "YES"
        break
        
# Write an answer using print
print(output)

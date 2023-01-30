import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = [ord(char.lower()) - ord('a') for char in list(input())]

for i in range(h):
    row = input()
    output = ''
    for i in t:
        i = i if 0 <= i < 26 else 26
        output += row [ i*l : (i+1) *l ]
    # Write an answer using print
    print(output)

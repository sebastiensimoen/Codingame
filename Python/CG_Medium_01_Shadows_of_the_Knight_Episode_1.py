import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

w0 = 0 
h0 = 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if "U" in bomb_dir: # UP
        h = y0
        y0 = (y0 + h0) / 2

    if "D" in bomb_dir: # DOWN
        h0 = y0
        y0 = (y0 + h) / 2

    if "L" in bomb_dir: #LEFT
        w = x0
        x0 = (x0 + w0) / 2

    if "R" in bomb_dir: # RIGHT
        w0 = x0
        x0 = (x0 + w) / 2

    # Write an action using print
    # the location of the next window Batman should jump to.
    print(int(x0), int(y0))

import sys
import math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.

# game loop
while True:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print
    # You have to output a correct ship name to shoot ("Buzz", enemy1, enemy2, ...)
    print(enemy_1 if dist_1 < dist_2 else enemy_2)https://www.codingame.com/training/easy/onboarding

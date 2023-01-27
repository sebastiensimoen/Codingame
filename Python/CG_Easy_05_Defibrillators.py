import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lonA = float(input().replace(",", "."))
latA = float(input().replace(",", "."))
dMin = sys.float_info.max

n = int(input())
for i in range(n):
    defib = input().split(";")
    lonB = float(defib[4].replace(",","."))
    latB = float(defib[5].replace(",","."))

    x = (lonB-lonA) * math.cos((latA+latB)/2)
    y = latB - latA
    d = math.sqrt(x**2 +y**2) * 6371

    if d < dMin:
        dMin = d
        defibName = defib[1]

# Write an answer using print
print(defibName)

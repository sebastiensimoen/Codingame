import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
tabExt = []
tabMt = []

for _ in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    tabExt.append(ext.lower())
    tabMt.append(mt)

for _ in range(q):
    fname = input()  # One file name per line.
    if("." in fname):
        fnameTab = fname.split(".")
        # Write an answer using print
        if (fnameTab[-1].lower() in tabExt):
            print(tabMt [ tabExt.index (fnameTab[-1].lower()) ] )
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")

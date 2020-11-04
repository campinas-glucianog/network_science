from random import random
import sys

N = 500
kbar = float(sys.argv[1])
p = kbar/(N-1)

print("*Vertices ", N)
print('*Edges')
for i in range(N):
    for j in range(1+1, N):
        if random() < p:
            print(i+1,j+1)
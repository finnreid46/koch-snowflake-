import numpy as np
import matplotlib.pyplot as plt

def expand(M):
    Z = np.zeros_like(M)
    return np.block([[Z, M, M],  #try chaning the positions of M and Z for new patterns.
                     [M, Z, M],
                     [M, M, Z]])

n = np.array([[0, 1, 1],
              [1, 0, 1],           # for recurssion make sure the 1's corrospond to the M's and 0's to Z's.
              [1, 1, 0]])

for _ in range(2):  #Keep small to avoid problems.
    n = expand(n)

points = set(zip(*np.where(n == 1)))            #
node_index = {point: i for i, point in enumerate(points)}          
plt.figure(figsize=(7,7))

#assigns the directions for the edges.
b = 2 # keep small to avoid problems. 
directions = [(0, b), (b, 0), (b, b), (b, -b)]

for r, c in points:
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if (nr, nc) in points:
            plt.plot([c, nc], [-r, -nr], linewidth=0.8)

# draws the nodes
x = [c for r, c in points]
y = [-r for r, c in points]
plt.scatter(x, y, s=8)

plt.gca().set_aspect('equal', 'box')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
s32 = np.sqrt(3) / 2
x = [0, 1, 0.5, 0]
y = [0, 0, s32, 0]
fig, ax = plt.subplots()
ax.plot(x, y, 'k-', linewidth=1.2, alpha=0.5)
N = 4
for n in range(N):
    x_new = []
    y_new = []
    for i in range(len(x) - 1):
        xa, ya = x[i], y[i]
        xb, yb = x[i+1], y[i+1]
        dx = (xb - xa) / 3
        dy = (yb - ya) / 3
        x1, y1 = xa + dx, ya + dy
        x2, y2 = xa + 2*dx, ya + 2*dy
        xm = xa + 1.5*dx + dy*s32
        ym = ya + 1.5*dy - dx*s32
        ax.plot([x1, xm, x2, x1], [y1, ym, y2, y1], 'r-', linewidth=0.7, alpha=0.7)
        x_new.extend([xa, x1, xm, x2])
        y_new.extend([ya, y1, ym, y2])
    x_new.append(x[-1])
    y_new.append(y[-1])
    x = x_new
    y = y_new
    ax.plot(x, y, 'b-', linewidth=1.0, alpha=0.6)
ax.set_aspect('equal', 'box')
plt.show()
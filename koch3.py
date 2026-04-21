import numpy as np
import matplotlib.pyplot as plt

def rotate(v, angle_deg):
    angle = np.radians(angle_deg)
    x, y = v
    return np.array([
        x*np.cos(angle) - y*np.sin(angle),
        x*np.sin(angle) + y*np.cos(angle)
    ])

def expand_segment(v):
    return [
        v/3,
        rotate(v/3, 60),
        rotate(v/3, -60),
        v/3
    ]

def build_path(iterations):
    path = [np.array([1.0, 0.0])]

    for _ in range(iterations):
        new_path = []
        for v in path:
            new_path.extend(expand_segment(v))
        path = new_path

    return path

def path_to_coords(path, start=(0.0, 0.0)):
    points = [np.array(start, dtype=float)]
    current = np.array(start, dtype=float)

    for v in path:
        current = current + v
        points.append(current.copy())

    return np.array(points)

def make_snowflake(iterations):
    side = build_path(iterations)

    side1 = side
    side2 = [rotate(v, -120) for v in side]
    side3 = [rotate(v,  120) for v in side]

    pts1 = path_to_coords(side1, start=(0.0, 0.0))
    pts2 = path_to_coords(side2, start=pts1[-1])
    pts3 = path_to_coords(side3, start=pts2[-1])

    # avoid repeating the joining points
    snowflake = np.vstack([pts1, pts2[1:], pts3[1:]])
    return snowflake

coords = make_snowflake(4)

plt.figure(figsize=(7,7))
plt.plot(coords[:,0], coords[:,1])
plt.gca().set_aspect('equal', 'box')
plt.show()
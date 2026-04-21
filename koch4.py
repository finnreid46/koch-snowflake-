import numpy as np, matplotlib.pyplot as plt
def R(v,a):
    a=np.radians(a); x,y=v
    return np.array([x*np.cos(a)-y*np.sin(a), x*np.sin(a)+y*np.cos(a)])
def K(n,v=np.array([1.,0.])):
    return [v] if n==0 else sum((K(n-1,v/3), K(n-1,R(v/3,60)), K(n-1,R(v/3,-60)), K(n-1,v/3)), [])
def C(path,p=(0,0)):
    pts=[np.array(p,float)]
    for v in path: pts.append(pts[-1]+v)
    return np.array(pts)
n=4
s=K(n)
a=C(s)
b=C([R(v,-120) for v in s], a[-1])
c=C([R(v,120) for v in s], b[-1])
pts=np.vstack([a,b[1:],c[1:]])
plt.plot(pts[:,0],pts[:,1])
plt.gca().set_aspect('equal','box')
plt.show()

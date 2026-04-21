import numpy as np, matplotlib.pyplot as plt
def r(v,a):
 a=np.radians(a);x,y=v;return np.array([x*np.cos(a)-y*np.sin(a),x*np.sin(a)+y*np.cos(a)])
def k(i,v=np.array([1.,0.])): return [v] if i<1 else sum((k(i-1,v/3),k(i-1,r(v/3,60)),k(i-1,r(v/3,-60)),k(i-1,v/3)),[])
def c(s,t=(0,0)):
 q=[np.array(t,float)]
 for v in s:q+=[q[-1]+v]
 return np.array(q)
s=k(4);a=c(s);b=c([r(v,-120)for v in s],a[-1]);d=c([r(v,120)for v in s],b[-1]);z=np.vstack([a,b[1:],d[1:]])
plt.plot(z[:,0],z[:,1]);plt.gca().set_aspect('equal','box');plt.show()
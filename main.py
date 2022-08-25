import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def f(s,t):
    a = -3 ; b = 3
    c = -2 ; d = 1
    R,J = s
    dRdt = a * R + b * J
    dJdt = c * R + d * J
    return [dRdt, dJdt]
t = np.linspace(0 , 10 ,200, endpoint=False) # a < t < b ,every 200 time
s0=[-4,2] # R0 -- J0
s = odeint(f,s0,t)
plt.plot(t,s[:,0])
plt.plot(t,s[:,1])
plt.xlabel("Time")
plt.ylabel("Love for the other")
plt.legend(["Romeo's","Juliet's"])
plt.savefig("bieudo.png")
plt.show()
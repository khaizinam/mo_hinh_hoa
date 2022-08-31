import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

R0 = 4
J0 = 4
def f(s,t):
    a = 1
    b = -2
    c = 1
    d = -2
    R,J = s
    dRdt = a * R + b * J
    dJdt = c * R + d * J
    return [dRdt, dJdt]
t = np.linspace(0 , 10 ,200, endpoint=False) # a < t < b ,every 200 time
s0=[R0,J0] # R0 -- J0
s = odeint(f,s0,t)
plt.plot(t,s[:,0])
plt.plot(t,s[:,1])
plt.xlabel("Time")
plt.ylabel("Love for the other")
plt.legend(["Romeo's","Juliet's"])
plt.show()
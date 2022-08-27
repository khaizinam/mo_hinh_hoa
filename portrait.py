
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# a b Style
# + + Eager Beaver
# + − Narcissistic Nerd
# − + Cautious Lover
# − − Hermit
#R = aR + bJ;
# delta < 0 [2 , 4, -2, -2] point [[-4, 2],[-4 , -1],[4,-1] ,[4,2]]
#delta > 0 [-3 ,3, -2, 1] point [[-4, 2],[-4 , -1],[4,-1] ,[4,2]]
Ci = [-3 ,3, -2, 1] 
Sts = [[-4, 2],[-4 , -1],[4,-1] ,[4,2]]

def ivpSys(s, t , a, b, c, d):
    R,J = s
    dRdt = a * R +b * J
    dJdt = c * R + d * J
    return [dRdt, dJdt]
a = Ci[0]
b = Ci[1]
c = Ci[2]
d = Ci[3]
# porttrait
y1 = np.linspace(-8, 8, 16)
y2 = np.linspace(-8, 8, 16)
Y1, Y2 = np.meshgrid(y1, y2)
t = 0
u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
NI, NJ = Y1.shape
for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = ivpSys([x, y], t, a, b, c, d)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]
Q = plt.quiver(Y1, Y2, u, v, color='g')
# trajector
tspan = np.linspace(0 , 10 ,200, endpoint=False)
for elementSt, St in enumerate(Sts):
    sol = odeint(ivpSys, St, tspan,args=(a, b, c, d))
    if elementSt == 0:
        color = "r"
    else :
        color = "b"
    plt.plot(sol[:,0], sol[:,1], color)
    plt.plot([sol[-1,0]], [sol[-1,0]], 'g',linewidth=5.0) # end
#--
plt.xlabel("Romeo's love for Juliet")
plt.ylabel("Juliet's love for Romeo")
plt.xlim([-4.5, 4.5])
plt.ylim([-4.5, 4.5])
plt.show()

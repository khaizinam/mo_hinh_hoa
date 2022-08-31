import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
###################################################
pi = math.pi
a = 2
b = 4
c = -2
d = 2
R0 = 5/4
J0 = 5/4
def delta(a,b,c,d):
    return pow((a + d), 2) - 4 * (a * d - b * c)
def lamda(a,b,c,d):
    deltaValue = delta(a,b,c,d)
    if deltaValue > 0 :
        deltaSqrt = math.sqrt(deltaValue)
        lamda1 = (a + b - deltaSqrt) / 2
        lamda2 = (a + b + deltaSqrt) / 2
        print("delta > 0 : lamda 1: "+str(lamda1)+", lamda2 : "+str(lamda2))
        return [lamda1 , lamda2]
    elif deltaValue == 0 :
        x = ( a + d ) / 2
        print("delta = 0 : lamda 1: "+str(lamda1)+", lamda2 : "+str(lamda2))
        return x
    else :
        deltaValue = abs(deltaValue)
        deltaSqrt = math.sqrt(deltaValue)
        a1 = ( a + d ) / 2
        b1 = deltaSqrt / 2
        print("delta < 0 : lamda: "+str(a1)+"+-"+str(b1)+"i")
        return [ a1, b1]
def Fxy(a,b,c,d,R0,J0 ,k1,k2):
    a1 = 1 ; b1 = 1 ; c1 = R0
    a2 = (k1 - a) ; b2 = (k2 - a) ; c2 = b * J0
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    print("C 1: "+str(Dx / D)+", C : "+str(Dy / D))
    return [Dx / D, Dy / D]
def Fxy2(a,b,c,d,R0,J0 ,k):
    a1 = 1 ; b1 = 0 ; c1 = R0
    a2 = (k - a) ; b2 = (1 - a) ; c2 = b * J0
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    print("C 1: "+str(Dx / D)+", C : "+str(Dy / D))
    return [Dx / D, Dy / D]
def Fxy3(a,b, R0,J0 , m, n):
    c1 = R0
    c2 = ((b * J0) - ((m - a ) * R0)) / n
    print("C 1: "+str(c1)+", C : "+str(c2))
    return [c1, c2]
def fR(t,a,b,c,d,R0,J0):
    deltaValue = delta(a,b,c,d)
    if deltaValue > 0:
        k1 = lamda(a,b,c,d)[0]
        k2 = lamda(a,b,c,d)[1]
        c1 = Fxy( a, b, c, d, R0, J0, k1, k2 )[0]
        c2 = Fxy( a, b, c, d, R0, J0, k1, k2 )[1]
        R = c1 * math.exp(k1 * t) + c2 * math.exp(k2 * t) 
        # print("k1 = " + str(k1)) 
        # print("k2 = " + str(k2)) 
        # print("c1 = " + str(c1)) 
        # print("c2 = " + str(c2)) 
        return R
    elif deltaValue == 0:
        k = lamda(a,b,c,d)
        c1 = R0
        c2 = Fxy( a, b, c, d, R0, J0, k)[1]
        R = c1 * math.exp(k * t) + c2 * math.exp(k * t) 
        # print("k1 = k2 = " + str(k)) 
        # print("c1 = " + str(c1)) 
        # print("c2 = " + str(c2)) 
        return R
    else :
        m = lamda(a,b,c,d)[0]
        n = lamda(a,b,c,d)[1]
        c1 = Fxy3(a,b, R0,J0 , m, n)[0]
        c2 = Fxy3(a,b, R0,J0 , m, n)[1]
        R = math.exp(m * t) * (c1 * math.cos((n * t)) + c2 * math.sin((n * t)))
        # print("k1 = " + str(m) + " +/- " + str(n)+"i") 
        # print("c1 = " + str(c1)) 
        # print("c2 = " + str(c2)) 
        return R
def fJ(t,a,b,c,d,R0,J0):
    deltaValue = delta(a,b,c,d)
    if deltaValue > 0:
        k1 = lamda(a,b,c,d)[0]
        k2 = lamda(a,b,c,d)[1]
        c1 = Fxy( a, b, c, d, R0, J0, k1, k2 )[0]
        c2 = Fxy( a, b, c, d, R0, J0, k1, k2 )[1]
        R = fR(t,a,b,c,d,R0,J0)
        dRdt = c1 * k1 * math.exp(k1 * t) + c2 * k2 * math.exp(k2 * t)
        J = (1 / b) * (dRdt - a * R) 
        return J
    elif deltaValue == 0:
        k = lamda(a,b,c,d)
        c1 = R0
        c2 = Fxy( a, b, c, d, R0, J0, k)[1]
        R = fR(t,a,b,c,d,R0,J0)
        dRdt = c1 * k * math.exp(k * t) + c2 * k * math.exp(k * t)
        J = (1 / b) * (dRdt - a * R)
        return J
    else :
        m = lamda(a,b,c,d)[0]
        n = lamda(a,b,c,d)[1]
        c1 = Fxy3(a,b, R0,J0 , m, n)[0]
        c2 = Fxy3(a,b, R0,J0 , m, n)[1]
        R = fR(t,a,b,c,d,R0,J0)
        dRdt = m * math.exp(m * t) * (c1 * math.cos((n * t)) + c2 * math.sin((n * t))) + math.exp(m * t) * (- (c1 * n * math.sin((n * t))) + (c2 * n * math.cos((n * t))))
        J = (1 / b) * ( dRdt - a * R ) 
        return J
###########################################
print(fR(2,a,b,c,d,R0,J0))
#print(fJ(1,a,b,c,d,R0,J0))
# t = np.linspace(0, 10, 100)
# Rt = np.vectorize(fR)
# Jt = np.vectorize(fJ)
# plt.plot(t,Rt(t,a,b,c,d,R0,J0))
# plt.plot(t,Jt(t,a,b,c,d,R0,J0))
# plt.xlabel("Time")
# plt.ylabel("Love for the other")
# plt.legend(["Romeo's","Juliet's"])
# plt.show()
from numpy import *
from sys import argv
import matplotlib.pyplot as plt

def powers(lst, p1, p2):
    return array([[v ** p for p in range(p1, p2 + 1)] for v in lst])

def poly(a, x):
    return sum([v * (x ** i) for i, v in enumerate(a)])

[X, Y] = transpose(loadtxt(argv[1]))

Xp  = powers(X,0,int(argv[2]))
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))[:,0]

X2 = linspace(min(X), max(X), (max(X) - min(X)) / 0.2).tolist()
Y2 = [poly(a, x) for x in X2]

plt.plot(X,Y,'ro')
plt.plot(X2,Y2)
plt.show()

from matrix import *
from sys import argv
import matplotlib.pyplot as plt

[X, Y] = transpose(loadtxt(argv[1]))

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = [b + m * v for v in X]

plt.plot(X,Y,'ro')
plt.plot(X, Y2)
plt.show()

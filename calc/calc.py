import random
import numpy as np
import matplotlib.pyplot as plt
'''
первые два бита:

00 - сложение
01 - вычитание
10 - умножение
11 - деление

вторые два бита: цифры

input shape: 4
hidden layer shape: 8
output shape: 1

'''
np.random.seed(2)
n0, n1, n2, n3 = 5, 64, 64, 1
w1 = np.random.randn(n1, n0) * np.sqrt(2/n0)
b1 = np.random.randn(n1, 1) * np.sqrt(2/n0)
w2 = np.random.randn(n2, n1) * np.sqrt(2/n1)
b2 = np.random.randn(n2, 1) * np.sqrt(2/n1)
w3 = np.random.randn(n3, n2) * np.sqrt(2/n2)
b3 = np.random.randn(n3, 1) * np.sqrt(2/n2)
ALFA = 0.01
m = 128
costs = []
iters = []

for i in range(1000):

    x = np.zeros((5,m))
    x[0] = np.random.uniform(-40, 40, (1,m))
    x[1] = np.random.uniform(-40, 40, (1,m))
    x[2] = x[0] * x[1]
    x[3] = x[0] / (x[1] + 0.00001)
    x[4] = np.around(np.random.uniform(0, 1, (1,m)))

    x[:4,:] = x[:4,:] / 40

    y = x[2] * x[4] + (x[0] + x[1]) * (x[4] == 0)

    x[:4,:] = x[:4,:] / 80

    z1 = np.dot(w1, x) + b1
    a1 = np.maximum(z1, 0)

    z2 = np.dot(w2, a1) + b2
    a2 = np.maximum(z2, 0)

    z3 = np.dot(w3, a2) + b3

    
    cost = (1/m) * np.sum(np.abs(z3 - y))
    print(cost)

    dz3 = (z3 - y)
    dw3 = (1/m) * np.dot(dz3, a2.T)
    db3 = (1/m) * np.sum(dz3, axis=1, keepdims=True)

    dz2 = np.dot(w3.T, dz3)
    dz2_deriv = dz2
    dz2_deriv[z2<0] = 0
    dw2 = (1/m) * np.dot(dz2_deriv, a1.T)
    db2 = (1/m) * np.sum(dz2_deriv, axis=1, keepdims=True)

    dz1 = np.dot(w2.T, dz2)
    dz1_deriv = dz1
    dz1_deriv[z1<0] = 0
    dw1 = (1/m) * np.dot(dz1_deriv, x.T)
    db1 = (1/m) * np.sum(dz1_deriv, axis=1, keepdims=True)

    w3 = w3 - ALFA * dw3 
    b3 = b3 - ALFA * db3

    w2 = w2 - ALFA * dw2 
    b2 = b2 - ALFA * db2

    w1 = w1 - ALFA * dw1
    b1 = b1 - ALFA * db1 

    if i % 10 == 0:
        costs.append(cost)
        iters.append(i)

fig = plt.subplots()  
plt.plot(iters, costs)
plt.show()


while True:
    x = np.zeros((4,1))
    x[0] = float(input())
    x[1] = float(input())
    x[2] = x[0]*x[1]
    x[3] = x[0]/x[1]

    z1 = np.dot(w1, x) + b1
    a1 = np.maximum(z1, 0)

    z2 = np.dot(w2, a1) + b2
    a2 = np.maximum(z2, 0)

    z3 = np.dot(w3, a2) + b3
    print(z3)






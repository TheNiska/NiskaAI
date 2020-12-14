import numpy as np
import sys
import math
import matplotlib.pyplot as plt

ALFA = 0.01
EPS = 0.000000001
iterations = 50
N_of_Words = 16
N_of_Letters = 21
V = N_of_Letters * N_of_Words
m = 300
cost_func = []
x_iter = []

sentenceX = np.zeros((V, m), dtype = float)
sentenceY = np.zeros((V, m), dtype = float)

f = open('adding.txt', 'r')
exemp = 0
for line in f:

	delim = line.find('=')
	x = line[0:delim].strip()
	y = line[delim+1:].strip()
	strX = x.lower()
	strY = y.lower()
	strX_list = strX.split() # массив слов вопроса
	strY_list = strY.split() # массив слов ответа

	i = 0
	for j in range(len(strX_list)):
		for k in range(len(strX_list[j])):
			sentenceX[i+k, exemp] = ord(strX_list[j][k])
		i += 21

	i = 0
	for j in range(len(strY_list)):
		for k in range(len(strY_list[j])):
			sentenceY[i+k, exemp] = ord(strY_list[j][k])
		i += 21
	exemp += 1

sentenceX = sentenceX / 1103
sentenceY = sentenceY / 1103
np.set_printoptions(threshold=sys.maxsize)
print(sentenceX.shape) # 336 x 300
print(sentenceY.shape) # 336 x 300
'''
word = ''
l = 0
for i in range(V):
	word = word + str(sentence[i,0]) + '||'
	l += 1
	if l == N_of_Letters:
		print(word)
		word = ''
		l = 0
'''

a0 = sentenceX
y = sentenceY

n0 = 336
n1 = 120
n2 = 60
n3 = 336

np.random.seed(1)

w1 = np.random.randn(n1, n0) * math.sqrt(1/n0)
b1 = np.random.randn(n1,1)

w2 = np.random.randn(n2,n1) * math.sqrt(1/n1)
b2 = np.random.randn(n2,1)

w3 = np.random.randn(n3,n2) * math.sqrt(1/n2)
b3 = np.random.randn(n3,1)

for o in range(iterations):
    proc = (o / iterations) * 100
    print( '{:.2f}'.format(proc), '%')
    
    z1 = np.dot(w1, a0) + b1
    a1 = np.tanh(z1)
    
    z2 = np.dot(w2, a1) + b2
    a2 = np.tanh(z2)
    
    z3 = np.dot(w3, a2) + b3
    a3 = z3

    J = (1/m) * np.sum(np.abs(a3 - y))
    print(J)

    cost_func.append(J)
    x_iter.append(o)


    dz3 = a3 - y
    dw3 = (1/m) * (np.dot(dz3, a2.T))
    db3 = np.sum(dz3, axis=1, keepdims=True) * (1/m)
    
    dz2 = np.dot(w3.T, dz3) * (1 - np.power(a2, 2))
    dw2 = (1/m) * (np.dot(dz2, a1.T))
    db2 = np.sum(dz2, axis=1, keepdims=True) * (1/m)
    
    dz1 = np.dot(w2.T, dz2) * (1 - np.power(a1, 2))
    dw1 = (1/m) * (np.dot(dz1, a0.T)) 
    db1 = np.sum(dz1, axis=1, keepdims=True) * (1/m)

    w3 = w3 - ALFA * dw3 
    b3 = b3 - ALFA * db3
    
    w2 = w2 - ALFA * dw2 
    b2 = b2 - ALFA * db2

    w1 = w1 - ALFA * dw1
    b1 = b1 - ALFA * db1  


fig = plt.subplots()  
plt.plot(x_iter, cost_func)
plt.show()

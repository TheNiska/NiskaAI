import numpy as np
import sys
import math
sys.path.append('../')
from letters.letters import *

words = np.array([['привет', 'пока', 'один', 'два', 'три', 'кораблекрушение',
                    'ложка', 'трапеция', 'шестьдесят', 'жёлтый']], dtype=str).T
print(words)
print(words.shape)

for j in range(words.shape[0]):
    wrd = words[j,0]
    word = np.ones((100, 1)) * -8

    i = 0
    for c in wrd:
        tmp = model_letters(c, False)
        for ii in range(4):
                word[i+ii, 0] = tmp[ii,0]
        i += 4

    if j == 0:
        x = word
    else:
        x = np.column_stack((x, word))

        if i > 96:
            break

X = x
Y = X


def random_init():
    np.random.seed(1)
    w1 = np.random.randn(200, 100) * math.sqrt(1/100)
    b1 = np.random.randn(200, 1) * 0.01
    w2 = np.random.randn(200, 200) * math.sqrt(1/200)
    b2 = np.random.randn(200, 1) * 0.01
    w3 = np.random.randn(100, 200) * math.sqrt(1/140)
    b3 = np.random.randn(100, 1) * 0.01

    return w1, b1, w2, b2, w3, b3

def propagate(w1, b1, w2, b2, w3, b3, X, Y):
    m = X.shape[1]

    z1 = np.dot(w1, X) + b1
    a1 = np.tanh(z1)

    z2 = np.dot(w2, a1) + b2
    a2 = np.tanh(z1)
    
    z3 = np.dot(w3, a2) + b3
    a3 = z3


    cost = (1/m) * np.sum(np.abs(a3 - Y))

    dz3 = a3 - Y
    dw3 = (1/m) * np.dot(dz3, a2.T)
    db3 = (1/m) * np.sum(dz3, axis=1, keepdims=True)

    dz2 = np.dot(w3.T, dz3) * (1 - np.power(a1, 2))
    dw2 = (1/m) * np.dot(dz2, a1.T)
    db2 = (1/m) * np.sum(dz2, axis=1, keepdims=True)

    dz1 = np.dot(w2.T, dz2) * (1 - np.power(a1, 2))     # 12 x 25
    dw1 = (1/m) * (np.dot(dz1, X.T))
    db1 = np.sum(dz1, axis=1, keepdims=True) * (1/m)

    return cost, dw1, db1, dw2, db2, dw3, db3

def optimize(w1, b1, w2, b2, w3, b3, X, Y, num_iterations, learning_rate):
    for i in range(num_iterations):
        cost, dw1, db1, dw2, db2, dw3, db3 = propagate(w1, b1, w2, b2, w3, b3, X, Y)
        w1 = w1 - learning_rate  * dw1
        b1 = b1 - learning_rate * db1
        w2 = w2 - learning_rate * dw2
        b2 = b2 - learning_rate * db2
        w3 = w3 - learning_rate * dw3
        b3 = b3 - learning_rate * db3
        print(cost)
    return w1, b1, w2, b2, w3, b3

w1, b1, w2, b2, w3, b3 = random_init()
w1, b1, w2, b2, w3, b3 = optimize(w1, b1, w2, b2, w3, b3, X, Y, 100000, 0.0003)
sys.path.append('\\words')
np.savetxt('word_recognizer_w1.txt', w1)
np.savetxt('word_recognizer_b1.txt', b1)
np.savetxt('word_recognizer_w2.txt', w2)
np.savetxt('word_recognizer_b2.txt', b2)
np.savetxt('word_recognizer_w3.txt', w3)
np.savetxt('word_recognizer_b3.txt', b3)

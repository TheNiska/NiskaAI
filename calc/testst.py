
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# N is batch size(sample size); D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 4, 2, 30, 1

# Create random input and output data
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 0.002
loss_col = []
for t in range(200):
    # Forward pass: compute predicted y
    h = x.dot(w1) # z1 = np.dot(w1, x)
    h_relu = np.maximum(h, 0)  # a1 = np.maximum(z1, 0)
    y_pred = h_relu.dot(w2) # z2 = np.dot(w2, a1)

    # Compute and print loss
    loss = np.square(y_pred - y).sum() # loss function
    loss_col.append(loss)
    print(t, loss, y_pred)

    # Backprop to compute gradients of w1 and w2 with respect to loss
    grad_y_pred = 2.0 * (y_pred - y) # the last layer's error # dz2
    grad_w2 = h_relu.T.dot(grad_y_pred) # = = np.dot(dz2, a1.T)

    grad_h_relu = grad_y_pred.dot(w2.T) # the second laye's error # dz1 = np.dot(w2.T, dz2)
    grad_h = grad_h_relu.copy() # copying dz1 
    grad_h[h < 0] = 0  # the derivate of ReLU # taking only 
    grad_w1 = x.T.dot(grad_h) # dw1 = np.dot(dz1, x.T)

    # Update weights
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2

plt.plot(loss_col)
plt.show()
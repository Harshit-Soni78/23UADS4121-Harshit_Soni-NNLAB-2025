# import math
import numpy as np
import nnfs

nnfs.init()

layer_outputs = [[4.8, 1.21, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]

# E = 2.71828182846
# E = math.e

exp_values = np.exp(layer_outputs)

# print(np.sum(layer_outputs, axis=1, keepdims=True))

'''
for output in layer_outputs:
    exp_values.append(E**output)

print(exp_values)

norm_base = sum(exp_values)
norm_values = []
for value in exp_values:
    norm_values.append(value / norm_base)

print(norm_values)
print(sum(norm_values))
'''

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

print(norm_values)
# print(np.sum(norm_values))

# Softmax Activation Function
# Exponential values are used to make all values positive
# Divide by sum of exponential values to normalize
# Output values are between 0 and 1
# Sum of output values is 1
# Used in classification problems
# Output values can be interpreted as probabilities

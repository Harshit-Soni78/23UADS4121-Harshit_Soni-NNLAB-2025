import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [0.2, 0.8, -0.5, 1.0]

bias = 2

# Output of current layer
output = np.dot(weights, inputs) + bias
print(output)


inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# Output of current layer
output = np.dot(weights, inputs) + biases
print(output)

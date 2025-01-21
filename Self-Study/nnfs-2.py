# Neural Network from Scratch - Part 2
'''
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

# Output of current layer
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias

print(output)
'''

# The above code is not scalable. It is not possible to add more inputs, weights and biases.
'''
inputs = [1.0, 2.0, 3.0, 2.5]

wights1 = [0.2, 0.8, -0.5, 1.0]
wights2 = [0.5, -0.91, 0.26, -0.5]
wights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

# Output of current layer
output = [inputs[0]*wights1[0] + inputs[1]*wights1[1] + inputs[2]*wights1[2] + inputs[3]*wights1[3] + bias1,
          inputs[0]*wights2[0] + inputs[1]*wights2[1] + inputs[2]*wights2[2] + inputs[3]*wights2[3] + bias2,
          inputs[0]*wights3[0] + inputs[1]*wights3[1] + inputs[2]*wights3[2] + inputs[3]*wights3[3] + bias3]

print(output)
'''

# The above code is not scalable. It is not possible to add more inputs, weights and biases.
'''
# The following code is scalable.
inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# Output of current layer
layer_outputs = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)
'''
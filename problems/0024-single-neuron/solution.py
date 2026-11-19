import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []

    for x in features:
        z = 0
        for i in range(len(weights)):
            z += x[i] * weights[i]

        z += bias

        p = 1 / (1 + math.exp(-z))
        probabilities.append(round(p, 4))

    mse = 0
    for i in range(len(labels)):
        mse += (probabilities[i] - labels[i]) ** 2

    mse = round(mse / len(labels), 4)

    return probabilities, mse
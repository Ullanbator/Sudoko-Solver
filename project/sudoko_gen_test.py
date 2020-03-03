import random
import numpy as np

firstMatrix = np.arange(9).reshape(3,3)

np.random.shuffle(firstMatrix)

print(firstMatrix)
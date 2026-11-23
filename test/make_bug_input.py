import numpy as np


input_data = np.zeros((20, 20))
input_data[-1, :] = 1
expected_data = np.arange(20)



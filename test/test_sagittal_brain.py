import numpy as np

import subprocess

input_data = np.zeros((20,20))
for row in range(20):
    input_data[row, :] = row
expected_data = np.arange(20)

np.savetxt("brain_sample.csv", input_data, fmt="%d", delimiter=",")
subprocess.run(["python", "sagittal_brain.py"])
output = np.loadtxt("brain_average.csv", delimiter=",")
np.testing.assert_array_equal(output, expected_data)



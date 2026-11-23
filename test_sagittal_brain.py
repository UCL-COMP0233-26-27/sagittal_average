import sys
import numpy as np
from sagittal_brain import run_averages   

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

# expected
data_expected = np.zeros((1, 20))
data_expected[0, -1] = 1

run_averages("brain_sample.csv", "brain_average.csv")

try:
    actual = np.loadtxt("brain_average.csv", delimiter=',')
except Exception as e:
    print("FAIL: cannot read output:", e)
    sys.exit(1)

if not np.allclose(actual, data_expected):
    print("FAIL: output mismatch")
    print("expected:", data_expected)
    print("actual:", actual)
    sys.exit(1)

print("PASS")
sys.exit(0)
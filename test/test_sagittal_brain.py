import numpy as np
import subprocess
import sys


def test_sagittal_brain():
    input_data = np.zeros((20, 20))

    for row in range(20):
        input_data[row, :] = row

    expected_data = np.arange(20)

    np.savetxt("brain_sample.csv", input_data, fmt="%d", delimiter=",")

    subprocess.run(
        [sys.executable, "-m", "sagittal_average.sagittal_brain"],
        check=True
    )

    output = np.loadtxt("brain_average.csv", delimiter=",")
    np.testing.assert_array_equal(output, expected_data)



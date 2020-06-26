# Solution Without Paralleization
import numpy as np
import time


start = time.time()

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size = [100000, 1000])
data = arr.tolist()

def examp01(row, minimum, maximum):
    """Returns how many numbers between `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

results = []
for row in data:
    results.append(examp01(row, minimum = 4, maximum = 8))

print('Serial execution:', results[:10])

print(f'Execution Time using serial code: {time.time() - start} seconds')
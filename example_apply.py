# native library import for python multiprocessing
import multiprocessing as mp
# efficient big data structure in python
import numpy as np
# measure algorithm performance using wall clocks
import time

def in_range_count(row, lowest, highest):
    '''Returns how many numbers lie within the lowest and highest in a given row'''
    counter = 0
    for item in row:
        if (lowest <= item <= highest):
            counter = counter + 1
    return counter

def generate_data():
	np.random.RandomState(100)
	arr = np.random.randint(0, 10, size = [100000, 1000])
	data = arr.tolist()
	return(data)

if __name__ == '__main__':
	
	start = time.time()
	
	# print("generating random data...")
	dataset = generate_data()

	# print("counting cores...")
	cpus = mp.cpu_count()
	
	# print("initializing multiprocessing pools...")
	pool = mp.Pool(cpus)
	
	# print("applying in_range_count to each row of data via pools...")
	lowest = 4
	highest = 8
	outcome = [pool.apply(in_range_count, args = (each_row, lowest, highest)) for each_row in dataset]

	# print("closing multiprocessing pools...")
	pool.close()    

	# print("printing counts of first 10 rows")
	rows_to_show_count = 10
	print(outcome[:rows_to_show_count])

	print(f'Execution Time pool.apply(): {time.time() - start} seconds')
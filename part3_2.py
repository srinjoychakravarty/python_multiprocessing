import numpy as np
import pandas as pd
import math
import multiprocessing as mp

def sum_of_squares(row):
	row_mean = sum(row) / len(row) 
	individual_deviations = [row[0] - row_mean, row[1] - row_mean]
	squared_deviations = [individual_deviations[0]**2, individual_deviations[1]**2]
	row_ss = sum(squared_deviations)
	row_standard_deviation = math.sqrt(row_ss)
	row_rounded_sd = round(row_standard_deviation, 2)
	return row_rounded_sd

def hypotenuse(row):
	hypotenuse = round(row[1]**2 + row[2]**2, 2)**0.5
	print(hypotenuse)
	return hypotenuse

if __name__ == '__main__':
	df = pd.DataFrame(np.random.randint(3, 10, size = [5, 2]))
	with mp.Pool(8) as pool:
		 result = pool.imap(sum_of_squares, df.itertuples(name = None), chunksize = 5)
		 output = [x for x in result]
	print(output)


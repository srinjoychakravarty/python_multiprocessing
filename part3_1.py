import numpy as np
import pandas as pd
import math

def sum_of_squares(row):
	row_mean = sum(row) / len(row) 
	individual_deviations = [row[0] - row_mean, row[1] - row_mean]
	squared_deviations = [individual_deviations[0]**2, individual_deviations[1]**2]
	row_ss = sum(squared_deviations)
	row_standard_deviation = math.sqrt(row_ss)
	row_rounded_sd = round(row_standard_deviation, 2)
	return row_rounded_sd

if __name__ == '__main__':
	list = []
	df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
	for row in df.itertuples(index = False):
		list.append(sum_of_squares(row))
	print(list)
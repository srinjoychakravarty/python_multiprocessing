import multiprocessing as mp

def normalize(list_c):
    minimum = min(list_c)
    maximum = max(list_c)
    return [(i - minimum)/(maximum - minimum) for i in list_c]

if __name__ == '__main__':
	list_c = [[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]]
	cpus = mp.cpu_count()
	pool = mp.Pool(cpus)
	results = [pool.apply(normalize, args=(l1, )) for l1 in list_c]
	pool.close()    
	print(results)
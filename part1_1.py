import multiprocessing as mp
import time

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

def common_intersection(list_A, list_B):
    return list(set(list_A).intersection(list_B))

def set_mathematics(list_A, list_B): 
    set_a = set(list_A) 
    set_b = set(list_B) 
    if (set_a & set_b): 
        return(set_a & set_b) 
    else: 
        return("No common elements")  

def multiprocessing_common_items(cpus):
	pool = mp.Pool(cpus)
	results = [pool.apply(set_mathematics, args = (list_A, list_B)) for list_A, list_B in zip(list_a, list_b)]
	pool.close()
	return(results)

def multiprocessing_common_items_2(cpus):
	pool = mp.Pool(cpus)
	results = [pool.apply(common_intersection, args = (list_A, list_B)) for list_A, list_B in zip(list_a, list_b)]
	pool.close()
	return(results)       

if __name__ == '__main__':
	cpus = mp.cpu_count()
	# print('Number of processsors in this machine: ', cpus)
	# print('Spawning multiple processes...')
	# print('Starting set maths stopwatch...')
	set_maths_timer_start = time.time()
	common_items = multiprocessing_common_items(cpus)
	set_maths_timer_end = time.time()
	set_maths_duration = set_maths_timer_end - set_maths_timer_start
	# print('Stopped set maths stopwatch!')
	# print('Multiple processes converged and ended!')
	# print('Spawning multiple processes...')
	# print('Starting list intersection stopwatch...')
	list_intersec_timer_start = time.time()
	common_items_2 = multiprocessing_common_items_2(cpus)
	list_intersec_timer_end = time.time()
	list_intersec_duration = list_intersec_timer_end - list_intersec_timer_start
	# print('Stopped list intersection stopwatch!')
	# print('Multiple processes converged and ended!')
	# print('Set maths common items result: ')
	print(common_items)
	print('Set maths wall time: ', set_maths_duration)
	# print('List intersection common items result: ')
	print(common_items_2)
	print('List intersection wall time: ', list_intersec_duration)
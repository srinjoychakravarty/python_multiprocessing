import os
import multiprocessing as mp

processes = ('script1.py', 'script2.py', 'script3.py')

def run_python(process):
    os.system('python3 {}'.format(process))

def main():
    pool = mp.Pool(processes = 3)
    pool.map(run_python, processes)

if __name__ == '__main__':
    main()


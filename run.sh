#!/bin/bash

echo "running pool.apply() to get the row wise common items in list_a and list_b..."
python3 part1_1.py
echo "running pool.map() to run script1 (crypto coin stats), script2 (ethereum vanity address) & script3 (protocol flags) in parallel..."
python3 part1_2.py
echo "running normalization of each row in 2d array between 0 and 1..."
python3 part1_3.py
echo "running serialized example..."
python3 example_ser.py
echo "running parallelization of pool.apply()..."
python3 example_apply.py
echo "running parallelization of pool.starmap()..."
python3 example_starmap.py
echo "running a function to sum the squares of each row and calculate the square root leaving two decimal places for the result..."
python3 part3_1.py
echo "running parallelized function with pool.imap()..."
python3 part3_2.py
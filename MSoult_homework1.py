"""
Michelle Soult
Fall 2014

Program to run selection sort 10 times each on arrays of four different sizes
Calculate min, max, and average running time for each set of runs
"""
import random
import time

def SelectionSort(arr, arr_size):
	""" Source = en.wikipedia.org/wiki/Selection_sort """
	index_min = 0
	for i in range (0, arr_size-1):
		index_min = i
		for j in range (i+1, arr_size):
			if(arr[j] < arr[index_min]):
				index_min = j
		if (index_min != i):
			temp_var = arr[i]
			arr[i] = arr[index_min]
			arr[index_min] = temp_var

def main():
	for i in range(0, 4):
		""" run four different rounds """
		print("Running Test", i, "...")
		arr_size = pow(10, (i+3))		#sizes will be 10^3 - 10^6
		
		max_time = 0		#need to keep track of running times
		min_time = 0
		curr_time = 0
		total_time = 0
		avg_time = 0
		
		
		for j in range(0, 10):
			""" run 10 different tests, with different random arrays """
			big_arr = []
			for k in range (0, arr_size):
				""" create array of appropriate size """
				new_rand = random.randint(0, 100000)
				big_arr.append(new_rand)
		
			time_start = time.clock()		#calculate running time
			SelectionSort(big_arr, arr_size)
			time_end = time.clock()
			curr_time = time_end - time_start
			
			total_time += curr_time			#update running times
			if (curr_time > max_time):
				max_time = curr_time
			if (j == 0) or (curr_time < min_time):
				min_time = curr_time
		
		avg_time = total_time/10
		print("For test", i, ":")
		print("The min running time was", min_time)
		print("The max running time was", max_time)
		print("The average running time was", avg_time, "\n")
		
main()

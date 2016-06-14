from max_subarray import MaxSubarray 
from max_subarray_bf import MaxSubarrayBF  
import random
import sys
import timeit
sample_array = [1]

def doMaxSubarray():
    res = MaxSubarray(sample_array, 0, len(sample_array))

def doMaxSubarrayBF():
    res = MaxSubarrayBF(sample_array, len(sample_array))

def main():
    avg_time = 0
    avg_n = 0
    for k in range(0, 1000):
        crossover = False
        crossover_point = 0
        time_taken = 0
        time_bf_taken = 0
        TR = timeit.Timer("doMaxSubarray()", "from __main__ import doMaxSubarray")
        TB = timeit.Timer("doMaxSubarrayBF()", "from __main__ import doMaxSubarrayBF")

        for i in range(2, 10000):
            global sample_array
            sample_array = []
            for j in range(0, i):
                sample_array.append(random.randint(0, 100))

            time_recurse = TR.timeit(number=1)
            time_bf = TB.timeit(number=1)
            if time_recurse < time_bf and crossover == False:
                crossover_point = i
                crossover = True 
                time_taken = time_recurse
                time_bf_taken = time_bf
                break

        print "crossover point: "+str(crossover_point)
        print "time taken: "+str(time_taken)
        print "time bf taken: "+str(time_bf_taken)

        avg_time += time_taken
        avg_n += crossover_point
    print "avg crossover point = "+str(avg_n//1000)
    print "avg time taken = "+str(avg_time/1000)

if __name__ == "__main__":
    sys.exit(main())
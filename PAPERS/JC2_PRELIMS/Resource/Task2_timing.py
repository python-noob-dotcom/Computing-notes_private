# import the built-in library time
import time
# use the function from Task 2.1 to generate 1000 integers
l1000 = task2_1(1000)
# use the perf_counter_ns() function to get two integers representing the start and end time
start = time.perf_counter_ns()
sorted_l1000 = task2_2(l1000)
task2_4(sorted_l1000)
end = time.perf_counter_ns()
# Calculate the duration, in nanoseconds (ns)
duration = end - start
print("Time (s):", duration / 10**9)

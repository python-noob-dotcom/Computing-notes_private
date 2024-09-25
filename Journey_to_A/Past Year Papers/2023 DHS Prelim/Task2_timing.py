# import the built-in library timeit 
import timeit 

# use the timeit function to call the task2_3() procedure & run it just once 
time2_3 = timeit.timeit(lambda: task2_3(), number=1)

# print out the time, in seconds
print(time2_3)

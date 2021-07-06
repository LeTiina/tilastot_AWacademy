import math
import statistics

#user inputs one line of numbers 1,2,3,4 etc.
line = input("Input a line of numbers for example:")

numbers = []
numbers = line.split(",")

sum = 0
for i in numbers:
    i = int(i)
    sum += i

smallest = min(numbers)
biggest = max(numbers)
how_many = len(numbers)
mean = round(sum/how_many,2)
mediaani = statistics.median(numbers)
moodi = statistics.mode(numbers)

print(f"Smallest one is {str(smallest)}. Biggest one is {str(biggest)}. Mean is {str(mean)}. Median is {str(mediaani)} and mode is {str(moodi)}.")
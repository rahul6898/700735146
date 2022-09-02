# List of Integers
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorting list of Integers
ages.sort()

print(ages)
# printing the maximum of 19,19,20,22,24,24,24,25,25,26
print("Maximum of 19,19,20,22,24,24,24,25,25,26 is : ",end="")
print (max(   19,19,20,22,24,24,24,25,25,26) )
# printing the minimum of 4,12,43.3,19,100
print("Minimum of 19,19,20,22,24,24,24,25,25,26 is : ",end="")
print (min(   19,19,20,22,24,24,24,25,25,26) )
ages.append(26)
ages.append(19)

# Import statistics Library
import statistics

# Calculate middle values
print(statistics.median([19,19,20,22,24,24,24,25,25,26]))
print(statistics.mean([19,19,20,22,24,24,24,25,25,26]))
ages.sort()
a1 = ages[0]
a2 = ages[len(ages)-1]
print(a2-a1)
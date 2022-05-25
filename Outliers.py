# This code strips the outlying values from an ordered data set.
# Checking with multiple data sets to check if it works fluently. Uncomment whichever data set you wish to try out the code with.

# Data Set 1: An empty data set
# data = [] 

# Data Set 2: Outlying values at low end only
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# Data Set 3: Outlying values at high end only
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

# Data Set 4: No outlying values 
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# Data Set 5: Only outlying values
# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]

# Data Set 6: Outlying values at both low and high end
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)     # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

print(start)    # for debugging
del data[start:]
print(data)

print("Arrays")

# Declaration
array = [10, 3, 7, 5]

# random indexing
print(array[0])
print(array[1])
print(array[:])
# print 0 till 2 exclusive
print(array[0:2])
# get last item
print(array[-1])

# can mix type
array = [10.9, 3, 7, 5, True]
print(array)

# Update
array[0] = 11.9
print(array)

# Traversal
array = [1, 2, 3]
max = array[0]
for num in array:
    if num > max:
        max = num
print(max)

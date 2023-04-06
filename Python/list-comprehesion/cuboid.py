x, y, z, n = int(input()), int(input()), int(input()), int(input())
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
print(coordinates)
#  start by reading in four integers x, y, z, and n from input, which represent the dimensions of the cuboid and the integer n respectively.

# We then create a list comprehension that generates all possible coordinates on the 3D grid using nested loops over the three dimensions i, j, and k. The range function is used to create ranges of values for each dimension, and the +1 is added to include the endpoint of the range.

# The if statement filters out any coordinates whose sum equals n, using a conditional expression.

# Finally, we print the list of coordinates.



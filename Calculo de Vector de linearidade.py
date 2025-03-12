import numpy as np
# Define the vectors
a = np.array([1, 1, 1])
b = np.array([1, 0, 2])
c = np.array([1, 2, 0])

# Create a matrix with the vectors as columns
matrix = np.column_stack((a, b, c))

# Calculate the rank of the matrix
rank = np.linalg.matrix_rank(matrix)

# Print the matrix and its rank
print("Matrix formed by vectors a, b, and c:")
print(matrix)
print(f"Rank of the matrix: {rank}")

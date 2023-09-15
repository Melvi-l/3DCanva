from Matrix4 import Matrix4

matrix = Matrix4(
    1,1,1,-1,
    1,1,-1,1,
    1,-1,1,1,
    -1,1,1,1
)
print(matrix)

print(matrix.getInverse())
vector1 = [2,4,5]
vector2 = [2,3,6]
# must be the same length

vector_multipicaion = []
for index in range(len(vector1)):
    vector_multipicaion.append(vector1[index] * vector2[index])
print(f"{vector1} * {vector2} is {vector_multipicaion}")

matrix1 = [[1,3,3] , [2,4], [2,3]]
matrix2 = [[5,2,3] , [1,0], [4,6]]
# must be the same size

matrix_add_result = []
for matrix_index in range(len(matrix1)):
    # take the vector out of the first matrix and add to the same vector in the second matrix 
    vector_add_result = []
    for vector_index in range(len(matrix1[matrix_index])):
        vector_add_result.append(matrix1[matrix_index][vector_index] + matrix2[matrix_index][vector_index])
    matrix_add_result.append(vector_add_result)

print(f"{matrix1} + {matrix2} = {matrix_add_result}")


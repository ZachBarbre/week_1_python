matrix1 = [[2,3] , [3,4]]
matrix2 = [[3,7] , [5,6]]
# must have len(matrix1) == len(matrix2[1]))
#answer = [21 , 45]

# [2,3] dot [3,5]
answer = []

answer.append(matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0])
answer.append(matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1])

print(answer)
# itterate over the first item in the list and interate over the 
# for vector_index in range(len(matrix1)):
#     temp_answer = 

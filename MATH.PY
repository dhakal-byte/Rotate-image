# we are getting to flip the image aka: the matrix in a 90 degree clockwise

# this is basic mathematics thing not a hard stuff

# so we have two options

# 1st : WITHOUT CONSIDERING SPACE COMPLEXITY
# we could create a new matrix and place values one by one
# TIME COMPLEXITY : O(N^2)
# SPACE COMPLEXITY : O(N^2)

# BUTTT...

# using transpose + reverse mathematical approach
# we can do it IN-PLACE (no extra matrix needed)
# TIME COMPLEXITY : O(N^2)
# SPACE COMPLEXITY : O(1)
# we are rotating a matrix 90 degree clockwise in-place

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # STEP 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # STEP 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# example tests 
matrix = [
    [1,            2,      3],
    [4,      5,     6],
    [7,    8,     9]
]

# create Solution object for bettermeamt 
obj = Solution()
obj.rotate(matrix)

# print t
print(matrix)
import math
# dummy data for user and item (user matrix)
userMatrix = [[5, 2, 3, 2, 4], [4, 3, 2, 0, 2],
              [3, 4, 1, 3, 0], [3, 5, 1, 2, 3]]
for user in userMatrix:
    print(user)

# calcualte the similarity matrix by pearson correlation (cosine similarity)
similarityMatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(similarityMatrix)

for i in range(0, len(userMatrix[0])):
    for j in range(i+1, len(userMatrix[0])):
        numerator = 0
        column1 = 0
        column2 = 0
        for k in range(0, len(userMatrix)):
            numerator += userMatrix[k][i]*userMatrix[k][j]
            column1 += userMatrix[k][i]*userMatrix[k][i]
            column2 += userMatrix[k][j]*userMatrix[k][j]
        denominator = math.sqrt(column1)*math.sqrt(column2)
        similarityMatrix[i][j] = numerator/denominator
        similarityMatrix[j][i] = numerator/denominator

for s in similarityMatrix:
    print(s)

item = int(input('what item you want to know?'))
user = int(input('what is the user?'))

item -= 1
user -= 1

num = 0
deno = 0
for i in range(0, len(userMatrix[0])):
    num += userMatrix[user][i]*similarityMatrix[i][item]
    deno += similarityMatrix[i][item]

print("the estimated rating is {}".format(num/deno))


import numpy as np

#행렬A
m = int(input("A행렬의 행수를 입력하세요"))
n = int(input("A행렬의 열수를 입력하세요"))

A_matrix = []

for i in range(1, m+1):
    ij_list = []
    for j in range(1, n+1):
        aij = float(input("A행렬의 성분 a{0}{1}를 입력하세요".format(i, j)))
        ij_list.append(aij)
    A_matrix.append(ij_list)
    

A = np.array(A_matrix)

print("\n")

#행렬B
m2 = int(input("B행렬의 행수를 입력하세요"))
n2 = int(input("B행렬의 열수를 입력하세요"))

B_matrix = []


for i2 in range(1, m2+1):
    ij_list2 = []
    for j2 in range(1, n2+1):
        aij2 = float(input("B행렬의 성분 b{0}{1}를 입력하세요".format(i2, j2)))
        ij_list2.append(aij2)
    B_matrix.append(ij_list2)
        
        
B = np.array(B_matrix)

print("\n")

print("A = \n",A) #A의 결과값

print("\n")

print("B = \n",B) #B의 결과값

print("\n")

#행렬합
sum_matrix = []
if n == n2 and m == m2:
    for k in range(1, m+1):
        matrix_sum = [i+j for i,j in zip(A[k-1], B[k-1])]
        sum_matrix.append(matrix_sum)
    S = np.array(sum_matrix)
    print("A+B =\n",S) #A+B의 결과값
else:
    print("덧셈이 불가능한 행렬입니다!")

print("\n")

#행렬곱
if n == m2:
    C = np.array([[0]*len(B[0]) for _ in range(len(A))])
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(A[0])): 
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    print("AxB =\n",C) #AxB의 결과값

else:
    print("곱셈이 불가능한 행렬입니다!")

print("\n")

#전치행렬
AT_m = []
for i in range(1, n+1):
    AT_matrix = []
    for k in range(1, m+1):
        AT_matrix.append(A[k-1][i-1])
    AT_m.append(AT_matrix)

AT = np.array(AT_m)
print("AT = \n",AT) #A의 전치행렬 AT

print("\n")

BT_m = []
for i in range(1, n2+1):
    BT_matrix = []
    for k in range(1, m2+1):
        BT_matrix.append(B[k-1][i-1])
    BT_m.append(BT_matrix)

BT = np.array(BT_m)
print("BT = \n",BT) #B의 전치행렬 BT

print("\n")

#행렬식
def determinant(matrix):

    if len(matrix) != len(matrix[0]):
        return "정사각행렬이 아니므로 행렬식 값이 존재하지 않습니다"

    else:
        if len(matrix) == 1:
            return matrix[0][0]

        elif len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        else:
            #기본행연산
            if matrix[0][0] != 0:
                for i in range(1, len(matrix)):
                    alpa = matrix[i][0]
                    for j in range(len(matrix)):
                        matrix[i][j] = matrix[i][j] - alpa*(matrix[0][j]/matrix[0][0])

                rate = matrix[0][0]
                matrix.remove(matrix[0])
                for k in range(len(matrix)):
                    matrix[k].remove(matrix[k][0])

                for p in range(len(matrix)):
                    matrix[0][p] = rate*matrix[0][p]

                return determinant(matrix)

            else:
                count = 0
                for i in range(len(matrix)):
                    if matrix[i][0] == 0:
                        count = count + 1
                        if count == len(matrix):
                            return 0
                    else:
                        change = matrix[i]
                        matrix[i] = matrix[0]
                        matrix[0] = change

                        for i in range(len(matrix)):
                            matrix[0][i] = -1*matrix[0][i]

                        return determinant(matrix)


print("|A| = det A = {0}".format(determinant(A_matrix)))
print("|B| = det B = {0}".format(determinant(B_matrix)))

print("\n")
















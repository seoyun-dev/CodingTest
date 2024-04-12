N, M = map(int, input().split())
sum = 0
sum_matrix = []
sum_nums = []

for row in range(N):
    nums = list(map(int, input().split()))
    for col in nums:
        if row == 0:
            sum += col
        else:
            sum += sum_matrix[row-2,N-1] + col
        sum_nums.append(sum)
    sum_matrix.append(sum_nums)
print(sum_matrix[1][2])
print(sum_matrix)

for _ in range(M):  
    x1,y1,x2,y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    if x1==0 and y1==0:
        print(sum_matrix[x2][y2])
    elif y1 == 0:
        print(sum_matrix[x2][y2]-sum_matrix[x1-1][N])
    else:
        print(sum_matrix[x2][y2]-sum_matrix[x1][y1-1])
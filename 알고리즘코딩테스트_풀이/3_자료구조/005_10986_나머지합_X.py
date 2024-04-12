import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sum = 0
sum_list = [0]

nums = map(int, input().split())
for num in nums:
    sum += num
    sum_list.append(sum%M)
print(sum_list)

count = 0
for i in range(N):
    for j in range(i+1, N+1):
        if sum_list[i] == sum_list[j]:
            count += 1
print(count)
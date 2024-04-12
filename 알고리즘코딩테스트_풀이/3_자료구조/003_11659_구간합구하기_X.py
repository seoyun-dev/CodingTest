import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sum = 0
sums = [0]
for i in nums:
	sum += i
	sums.append(sum)

for _ in range(M):
	i, j = map(int, input().split())
	print(sums[j]-sums[i-1])
num = int(input())
scores = list(map(int, input().split()))

best = max(scores)

print(sum(scores)/best*100/num)
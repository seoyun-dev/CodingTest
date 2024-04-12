num = int(input("더할 숫자의 개수: "))
str = input()
number = list(map(int, [i for i in str]))

sum = 0
for i in number[:num]:
    sum += i

print(sum)
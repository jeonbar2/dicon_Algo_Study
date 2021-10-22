N = int(input())
A = list(map(int, input().split()))
min = A[0]
max = A[0]
for i in A:
    if min > i:
        min = i
    if max < i:
        max = i

print(min, max)

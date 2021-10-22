N = int(input())
A = list(map(int, input().split()))
temp = max(A)
ans = 0
for i in A:
    ans += i / temp * 100
print(ans / N)

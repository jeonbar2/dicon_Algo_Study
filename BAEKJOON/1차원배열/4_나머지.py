A = []
for i in range(10):
    temp = int(input())
    if temp % 42 not in A:
        A.append((temp) % 42)
print(len(A))

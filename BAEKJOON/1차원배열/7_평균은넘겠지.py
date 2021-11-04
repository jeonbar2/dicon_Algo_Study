c = int(input())
answer = []
for i in range(c):
    A = list(map(int, input().split()))
    temp = 0
    n = 0
    for i in range(1, len(A)):
        temp += A[i]
    temp /= A[0]
    for i in range(1, len(A)):
        if A[i] > temp:
            n += 1

    answer.append(round(float(n / A[0]) * 100, 3))
for i in answer:
    print(format(i, ".3f"), "%", sep="")

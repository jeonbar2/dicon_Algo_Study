def LessX(N, X):
    A = list(map(int, input().split()))
    for i in range(N):
        if X > A[i]:
            print(A[i], end=" ")


N, X = map(int, input().split())
LessX(N, X)

def CountingStars(N):
    for i in range(1, N + 1):
        print(" " * (N - i) + "*" * i)


N = int(input())
CountingStars(N)

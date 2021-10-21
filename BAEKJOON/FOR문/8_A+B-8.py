def sum(i, A, B):
    print("Case #", i, ": ", A, " + ", B, " = ", A + B, sep="")


T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    sum(i + 1, A, B)

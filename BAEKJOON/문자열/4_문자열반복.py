T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    S = str(S)

    for J in S:
        print(J * R, end="")
    print()

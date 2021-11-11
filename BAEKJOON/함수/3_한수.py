def x(n):
    ##한수이면 트루##
    if (int(int(str(n)[0]) + int(str(n)[2])) / 2) == int(str(n)[1]):
        return True


n = int(input())

cnt = 0
if n > 99:
    cnt = 99
    for i in range(100, n + 1):
        if x(i):
            cnt += 1
else:
    cnt = n


print(cnt)

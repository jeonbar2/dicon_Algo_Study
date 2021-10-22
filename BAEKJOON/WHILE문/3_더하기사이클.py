def cycle(N):
    cnt = 0
    temp = N
    while 1:
        if temp < 10:
            temp = temp * 10 + temp

        else:
            temp = 10 * (temp % 10) + ((temp // 10 + temp % 10) % 10)

        cnt += 1

        if temp == N:
            break
    return cnt


print(cycle(int(input())))

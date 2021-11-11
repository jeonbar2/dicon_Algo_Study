def d(n):
    temp = 0
    temp += n
    while n > 0:
        temp += n % 10
        n = n // 10
    return temp


s_list = [False] * 10000

for i in range(1, 10000):
    if d(i) >= 10000:
        continue
    s_list[d(i)] = True

for i in range(1, 10000):
    if s_list[i] == False:
        print(i)

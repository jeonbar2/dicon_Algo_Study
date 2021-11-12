a = list(range(97, 123))
A = list(range(65, 91))
temp = [0] * 26
s = input()
for i in A:
    temp[i - 65] += s.count(chr(i))


for i in a:
    temp[i - 97] += s.count(chr(i))


cnt = 0
for i in temp:
    if i == max(temp):
        cnt += 1
        ans = chr(temp.index(i) + 65)

if cnt == 1:
    print(ans)
else:
    print("?")

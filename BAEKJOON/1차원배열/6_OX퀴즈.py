T = int(input())

for i in range(T):
    s = list(input())
    a = [0] * len(s)
    for j in range(len(s)):

        if j == 0:
            if s[j] == "O":
                a[j] = 1
            else:
                a[j] = 0

        else:
            if s[j - 1] == "O":
                if s[j] == "O":
                    a[j] = a[j - 1] + 1
                else:
                    a[j] = 0

            else:
                if s[j] == "O":
                    a[j] = 1
                else:
                    a[j] = 0
    print(sum(a))

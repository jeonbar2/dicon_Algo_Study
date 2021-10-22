def sum(a, b):
    print(a + b)


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        sum(a, b)

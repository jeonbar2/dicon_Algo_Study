def sum(a, b):
    print(a + b)


while True:
    try:
        a, b = map(int, input().split())
        sum(a, b)
    except:
        break

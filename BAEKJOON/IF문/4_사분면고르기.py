x = int(input())
y = int(input())


def Quadrant(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3


print(Quadrant(x, y))

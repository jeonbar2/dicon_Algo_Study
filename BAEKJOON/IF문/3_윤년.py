year = int(input())


def Leapyear(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return 1
    return 0


print(Leapyear(year))

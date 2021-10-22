A = int(input())
B = int(input())
C = int(input())

temp = A * B * C
l = []
while temp != 0:
    l.append(temp % 10)
    temp //= 10


for i in range(0, 10):
    print(l.count(i))

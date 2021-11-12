s = input()
b = list(range(97, 123))

c = []
for i in b:
    print(s.find(chr(i)), end=" ")

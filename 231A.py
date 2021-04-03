t = int(input())
counter = 0
for i in range(t):
    x, y, z = map(int, input().split())
    #print(y)
    if (x + y + z) >= 2:
        counter = counter + 1
    if (x + y + z) < 2:
        counter = counter
print(counter)
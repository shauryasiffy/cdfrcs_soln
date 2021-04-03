M, N= map(int, input().split())
p = M * N
if p % 2 == 0:
    print(int(p/2))
if p % 2 != 0:
    print(p//2)
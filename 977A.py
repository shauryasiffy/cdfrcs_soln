a,k=list(map(int, input().split(" ")))
for _ in range(0,k):
    result=0
    if a%10==0:
        a=a/10
    else:
        a=a-1
print(int(a))

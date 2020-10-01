
for _ in range(int(input())):
    x=int(input())
    y=list(map(int,input().split()))
    max=0
    for i in range(x-1):
        if y[i+1]>y[i]:
            y[i+1]=y[i]
        else:
            max+=1
    print(max)

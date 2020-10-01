for _ in range(int(input())):
    n=int(input())
    lis= list(map(int,input().split()))
    skip_strings=0
    for i in range(n-1):
        skip_strings+= lis[i+1] -lis[i] -1
    print(skip_strings)

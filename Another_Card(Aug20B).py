import math
for _ in range(int(input())):
    Pc,Pr = map(int, input().split())
    Pr = math.ceil(Pr/9)
    Pc = math.ceil(Pc/9)
    if Pr <= Pc:
        print(1,Pr)
    else:
        print(0,Pc)

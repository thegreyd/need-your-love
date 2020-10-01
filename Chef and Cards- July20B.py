def count(i):
    c = 0
    for __ in range(len(i)):
        c+=int(i[__])
    return c


for _ in range(int(input())):
    chef= 0
    morty= 0
    for k in range(int(input())):
        a,b = input().split()
        if count(a)>count(b):
            chef+=1
        elif count(a)<count(b):
            morty+=1
        else:
            chef += 1
            morty += 1
    if chef > morty:
        print(0, chef)
    elif chef < morty:
        print(1, morty)
    else:
        print(2, chef)
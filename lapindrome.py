z=int(input())
for i in range(z):
          s=input()
          s1=s[:len(s)//2]
          s2=s[(len(s)+1)//2:]
          try:
                    for i in s1:
                              t=s2.index(i)
                              s2=s2[:t]+s2[t+1:]
                    print("YES")
          except ValueError:
                    print("NO")
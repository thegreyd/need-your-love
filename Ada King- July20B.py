for _ in range(int(input())):
    temp = ["O"]
    for __ in range(int(input())):
        temp.append(".")
    temp+= ["X"]*(64-len(temp))
    chess,k =[], 0
    for i in range(8):
        temp2=[]
        for j in range(8):
            temp2.append(temp[k])
            k+=1
        chess.append(temp2)
    print('\n'.join([''.join([item for item in row])
                     for row in chess]),"\n")

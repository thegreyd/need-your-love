T = int(input())
while T>0:
	row,col = map(int,input().split())
	M,walls,wall=[],[],'#'
	for j in range(row):
		A = input()
		walls.extend([(j,i) for i, x in enumerate(A) if x == wall])
		M.append(A)
	mnstr=[(x,y) for x in range(2,row-2) for y in range(2,col-2)]
	for (x,y) in walls:
		a=[(x,y),(x-1,y),(x-2,y),(x+1,y),(x+2,y),(x,y-1),(x,y-2),(x,y+1),(x,y+2)]
		for i in a:
			if i in mnstr:
				mnstr.remove(i)
	print(len(mnstr))
	T-=1
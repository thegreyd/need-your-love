from itertools import imap
T = int(raw_input())
while T>0:
	row,col = imap(int,raw_input().split())
 	M,walls=[],[]	
	wall=u'#'
 
	for j in xrange(row):
		A = raw_input()
 		walls.extend([(j,i) for i, x in enumerate(A) if x == wall])
 		M.append(A)
 

	mnstr=[(x,y) for x in xrange(2,row-2) for y in xrange(2,col-2)]
 	
 	for (x,y) in walls:
 		a=[(x,y),(x-1,y),(x-2,y),(x+1,y),(x+2,y),(x,y-1),(x,y-2),(x,y+1),(x,y+2)]
 		for i in a:
 			if i in mnstr:
 				mnstr.remove(i)
 
	print len(mnstr)
 	T-=1

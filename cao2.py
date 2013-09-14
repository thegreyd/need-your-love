import sys

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 
131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269]

def cao2():
	I = int(input())
	while I>0:
		row,col = map(int,input().split())
		M,walls=[],[]
		wall='#'

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

	
		mnstrs=0
		for x,y in mnstr:
			val=[]
			
			l,L=y-1,0
			while l>=0:
				if M[x][l]==wall:
					break
				L+=1
				l-=1
			val.append(L)
		
			if 2 not in val:		
				r,R=y+1,0
				while r<col:
					if M[x][r]==wall:
						break
					R+=1
					r+=1
				val.append(R)
			
			if 2 not in val:
				t,T=x-1,0
				while t>=0:
					if M[t][y]==wall:
						break
					T+=1
					t-=1
				val.append(T)
			
			if 2 not in val:
				b,B=x+1,0
				while b<row:
					if M[b][y]==wall:
						break
					B+=1
					b+=1
				val.append(B)
				
			base=min(val)
			for x in primes:
				if x<=base:
					mnstrs+=1
				else:
					break
		print(mnstrs)
		I-=1
cao2()
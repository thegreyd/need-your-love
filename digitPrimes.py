def checkPrime(n):
	for x in range(2,int(n**0.5)+1):
		if not n%x:
			return False
	return True
def generatePrimes(up,low):
	plist=[]
	for x in range(up,low+1):
		if checkPrime(x):
			plist.append(x)
	return plist
def digitSum(n):
	sum=0
	while n:
		sum+=n%10
		n//=10
	return sum
def generatedigitPrimes(up,low):
	dplist=[]
	primeslist=generatePrimes(up,low)
	for x in primeslist:
		if checkPrime(digitSum(x)):
			dplist.append(x)
	return dplist

def main():
	s=input().split(" ")
	uplim=int(s[0])
	lowlim=int(s[1])
	index=int(s[2])
	dprimes=generatedigitPrimes(uplim,lowlim)
	print(dprimes)
	if index<len(dprimes):
		print(dprimes[index])
	else:
		print("No number at this index")
main()

def arug():
	print(s) for s in range(1,10)
arug()	


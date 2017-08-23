import time
import numpy as np

def split(number,n):

	number=str(number)
	if len(number)<n:
		number="".join(['0' for i in range(n-len(number))])+number
	
	hi=int(number[0:int(n/2)])
	lo=int(number[int(n/2):n])
	return hi,lo

	
def karatsuba(n1,n2):
	
	
	if n1<10 or n2<10:
		return n1*n2
	
	n=max(len(str(n1)),len(str(n2)))
	if n%2==1:
		n=n+1
	n_2=int(n/2)

	hi1,lo1=split(n1,n)
	hi2,lo2=split(n2,n)
	
	z0=karatsuba(lo1,lo2)
	z1=karatsuba(lo1+hi1,lo2+hi2)
	z2=karatsuba(hi1,hi2)
	
	value=(z2*(10**n))+((z1-z2-z0)*(10**n_2))+z0
	return value
	
	
if __name__=="__main__":
	
	start=time.time()
	num1=3141592653589793238462643383279502884197169399375105820974944592
	num2=2718281828459045235360287471352662497757247093699959574966967627
	end=time.time()

	print(karatsuba(num1,num2))
	print(end-start," s")

# calculates the number of inversions while merging x and y given that x and y are sorted arrays
def splitInvCount(x,y):

	count,i,j=0,0,0
	lx,ly=len(x),len(y)

	result=list()
	
	for ind in range(lx+ly):
		
		if i==lx or j==ly:
			if i==lx:
				result=result+y[j::]
				
			else:
				result=result+x[i::]
				
			return result,count
			
		if x[i]<=y[j]:
			result.append(x[i])
			i=i+1
		else:
			result.append(y[j])
			j=j+1
			count=count+lx-i
	return result,count
			
			


def split(x):
	n=len(x)
	if n%2==0:
		return x[0:int(n/2)],x[int(n/2):n]
	else:
		return x[0:int(n/2)+1],x[int(n/2)+1:n]
		

def countInversion(x):
	
	# For an array of size less than 1, there is no inversion
	count=0
	if len(x)<=1:
		return x,0
	elif len(x)==2:
		return splitInvCount([x[0]],[x[1]])
	
	L,R=split(x)
	
	
	l1,c1=countInversion(L)
	l2,c2=countInversion(R)
	l3,c3=splitInvCount(l1,l2)
	
	return l3, c1+c2+c3
	
	
	

if __name__=="__main__":
	#data=[4,3,5,1,8,7,6,2,18,17,16,15,14]
	data=list()
	with open("IntegerArray.txt") as file:
		for line in file: 
			line=line.strip()
			data.append(int(line))
        	
    	
	arr,count= countInversion(data)
	print(count)
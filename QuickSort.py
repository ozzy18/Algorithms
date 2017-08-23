### pivot as the first element
def quicksort1(x):
	
	size=len(x)
	count=size-1
	
	##base case
	if size<=1:
		return x,count
	
	pivot=x[0]
	i=1

	
	for j in range(count):

		
		if x[j+1]<pivot:
			
			x[i],x[j+1]=x[j+1],x[i]
			i=i+1
	pivot_pos=i-1
	x[0],x[pivot_pos]=x[pivot_pos],x[0]
	c1,c2=0,0
	if i>1:
		x[0:i-1],c1=quicksort1(x[0:i-1])
	if i<size:
		x[i:size],c2=quicksort1(x[i:size])

	return x,count+c1+c2
	
####### pivot as the last element
def quicksort2(x):
	
	size=len(x)
	count=size-1
	
	##base case
	if size<=1:
		return x,count
	
	pivot=x[count]
	x[0],x[count]=x[count],x[0]
	i=1

	
	for j in range(count):

		
		if x[j+1]<pivot:
			
			x[i],x[j+1]=x[j+1],x[i]
			i=i+1
	pivot_pos=i-1
	print(x)
	x[0],x[pivot_pos]=x[pivot_pos],x[0]
	
	print(pivot,x)
	c1,c2=0,0
	if i>1:
		x[0:i-1],c1=quicksort2(x[0:i-1])
	if i<size:
		x[i:size],c2=quicksort2(x[i:size])

	return x,count+c1+c2		
	
### pivot as the median of three
def quicksort3(x):
	
	size=len(x)
	count=size-1
	
	##base case
	if size==1:
		return x,count
	if size==2:
		if x[0]>x[1]:
			x[0],x[1]=x[1],x[0]
		return x,count
	######################
	
	### determine the pivot-median of the first,middle and the last element
	
	if size%2==0:
		middle=int(size/2)-1
	else:
		middle=int((size+1)/2)-1
		
	
	xmin=min([x[0],x[middle],x[count]])
	xmax=max([x[0],x[middle],x[count]])
	
	
	pivot=x[0]
	for i in [0,middle,count]:
		if xmin<x[i]<xmax:
			pivot=x[i]
			x[i],x[0]=x[0],x[i]
	###############################
	
	i=1
	for j in range(count):

		
		if x[j+1]<pivot:
			
			x[i],x[j+1]=x[j+1],x[i]
			i=i+1
	pivot_pos=i-1
	x[0],x[pivot_pos]=x[pivot_pos],x[0]
	
	#print(pivot,x)
	c1,c2=0,0
	if i>1:
		x[0:i-1],c1=quicksort3(x[0:i-1])
	if i<size:
		x[i:size],c2=quicksort3(x[i:size])

	return x,count+c1+c2

if __name__=="__main__":
	x=[2,3,5,7,9,10]
	data=list()
	with open("QuickSort.txt") as file:
		for line in file: 
			line=line.strip()
			data.append(int(line))
	
	
	print (quicksort1(data)[1])
## This code implements the randomized contraction algorithm for the mincut problem

from random import randrange
import random
import copy

def contract(G):


	while len(G)>2:
			
		n=len(G)
		rand_index=randrange(0,n)
		v1=G[rand_index][0]
		item1=G[rand_index]
	
		m=len(G[rand_index])
		rand_index2=randrange(1,m)
		v2=G[rand_index][rand_index2]
		

		for i in range(n):
	

			if v2 in G[i][0]:
				index=i
				v2=G[i][0]
				v2_edges=[x for x in G[index][1:len(G[index])] if x not in v1]
				v1_edges=[x for x in G[rand_index][1:len(G[rand_index])] if x not in v2]
				G.remove(G[index])
				G.remove(item1)
			
				edges=[]
				edges.append(v1+v2)
				edges=edges+list(set(v1_edges+v2_edges))
				G.append(edges)
				break
	value=max(len(G[0]),len(G[1]))
	return value-1
	
	
def multi_run(data,number_of_times):
	value=float("inf")
	
	for i in range(number_of_times):
		random.seed(i)
		temp_data=copy.copy(data)
		result=contract(temp_data)
		if result<value:
			value=result
			print(value)
	return value
			


if __name__=="__main__":
	
	#construct a list of lists--adjacency list
	# first element in each list is a vertex
	#my_data=[[[1],2,3,5],[[2],1,4],[[3],1,6],[[4],2,5],[[5],1,4,6],[[6],3,5]]
	data=[]
	with open("kargerMinCut.txt") as file:
		for line in file: 
			line=line.strip().split()
			line[0]=[line[0]]
			data.append(line)
	#data=my_data
	result=multi_run(data,1000)
	print(result)
	
	
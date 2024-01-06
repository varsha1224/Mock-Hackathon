# To find the closest path from the restaurant to all 20 neighborhoods
import json
from sys import maxsize 
from itertools import permutations

# Read the json file
f = open('C:/Mock Hackathon/Input data/level0.json')
data = json.load(f)
#print(data)

n0 = data['neighbourhoods']['n0']['distances']
#print(n0)
	
r0 = data['restaurants']['r0']['neighbourhood_distance']


# Find the shortest path from the restaurant at Saibaba colony, cover all 20 neighbourhoods and return back 
# function to implement traveling salesman 
V = 20

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	min_path = maxsize 
	next_permutation = permutations(vertex)
	for i in next_permutation:
        
		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		# update minimum 
		min_path = min(min_path, current_pathweight) 
		
	return min_path 

graph = []
graph.append(r0)	
j = 0
for i in range(19):
	start = [r0[j]]
	graph.append(start + data['neighbourhoods']['n' + str(i)]['distances'])
	j += 1
print(graph)
source = 0
print(travellingSalesmanProblem(graph, source))
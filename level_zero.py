# To find the closest path from the restaurant to all 20 neighborhoods
import json
import numpy as np
from sys import maxsize 
from itertools import permutations

# Read the json file
f = open('C:/Mock Hackathon/Input data/level0.json')
data = json.load(f)
#print(data)

n0 = data['neighbourhoods']['n0']['distances']
#print(n0)
	
r0 = data['restaurants']['r0']['neighbourhood_distance']

def findNextNode(arr, visited):
	n = len(arr)
	minVal = float('inf')
	for i in range(n):
		if arr[i] != 0 and arr[i] < minVal:
			if i not in visited:
				minVal = arr[i]
				nodeToVisit = i
	return nodeToVisit

graph = []
graph.append([0] + r0)	
j = 0
for i in range(20):
	start = [r0[j]]
	graph.append(start + data['neighbourhoods']['n' + str(i)]['distances'])
	j += 1

for i in range (len(graph)):
	print(graph[i])

visited = [0]
nodeToVisit = findNextNode(graph[0], visited)
visited.append(nodeToVisit)

print(len(graph[0]))
while len(visited) < 21:
	nodeToVisit = findNextNode(graph[nodeToVisit], visited) 
	visited.append(nodeToVisit)

#print(visited)
path = []
for i in range(len(visited)):
	if visited[i] == 0:
		path.append("r" + str(visited[i]))
	else:
		path.append("n" + str(visited[i] - 1))
path.append("r0")
print(path)

path_dict = {}
path_dict["path"] = path

json_object = {}
json_object["v0"] = path_dict

print(json_object)

with open("level0_output.json", "w") as outfile:
    json.dump(json_object, outfile)
# To find the closest path from the restaurant to all 20 neighborhoods
import json

# Read the json file
f = open('C:/Mock Hackathon/Input data/level1a.json')
data = json.load(f)

r0 = data['restaurants']['r0']['neighbourhood_distance']

graph = []
graph.append([0] + r0)
j = 0
orderQty = [0]		# will only have for indices n0 to n19 (r0 will not be present)
for i in range(20):
	start = [r0[j]]
	graph.append(start + data['neighbourhoods']['n' + str(i)]['distances'])
	orderQty.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])
	j += 1
	
capacity = data['vehicles']['v0']['capacity']
print(capacity)

for i in graph:
	print(i)
	
print(len(graph[0]))

def findNextNode(arr, visited, allVisited, capacityLeft, orderQty):
	n = len(arr)
	minVal = float('inf')
	for i in range(n):
		if arr[i] != 0 and arr[i] < minVal and orderQty[i] < capacityLeft:
			if i not in visited and i not in allVisited:
				minVal = arr[i]
				nodeToVisit = i
	return nodeToVisit, (capacityLeft - orderQty[nodeToVisit])

allPath = []	# Stores all the paths 
allVisited = []		# Stores all the nodes that has been visited
visited = [0]		# Each individual paths
capacityLeft = capacity
nodeToVisit, capacityLeft = findNextNode(graph[0], visited, allVisited, capacityLeft, orderQty)
visited.append(nodeToVisit)
print(visited)

while len(allVisited) < 21:
	while capacityLeft > 0:
		nodeToVisit, capacityLeft = findNextNode(graph[nodeToVisit], visited, allVisited, capacityLeft, orderQty) 
		visited.append(nodeToVisit)
	capacityLeft = capacity
	print(visited)
	allPath.append(visited)

#print(allPath)

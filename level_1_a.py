# To find the closest path from the restaurant to all 20 neighborhoods
import json

# Read the json file
f = open('C:/Mock Hackathon/Input data/level1a.json')
data = json.load(f)
#print(data)

n0 = data['neighbourhoods']['n0']['distances']
#print(n0)
	
r0 = data['restaurants']['r0']['neighbourhood_distance']

def checkIfPossible(capacityLeft, orderQty):
	if any(x <= capacityLeft for x in orderQty):
		return True
	else:
		return False

def findNextNode(arr, capacityLeft, orderQty, visited, allVisited):
    n = len(arr)
    minVal = float('inf')
    nodeToVisit = None  # Initialize nodeToVisit before the loop
    for i in range(n):
        if i in visited or i in allVisited:
            continue
        if arr[i] != 0 and arr[i] < minVal and capacityLeft >= orderQty[i]:
            minVal = arr[i]
            nodeToVisit = i
    if nodeToVisit is not None:  # Check if nodeToVisit has been assigned a value
        capacityLeft = capacityLeft - orderQty[nodeToVisit]
    return nodeToVisit, capacityLeft


orderQty = [0]	
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
#print(capacity)

allPath = []	        # Stores all the paths 
allVisited = []		    # Stores all the nodes that has been visited
visited = [0]		    # Each individual paths
capacityLeft = capacity
nodeToVisit, capacityLeft = findNextNode(graph[0], capacityLeft, orderQty, visited, allVisited)
print(nodeToVisit, capacityLeft)

while len(allVisited) < 21:
	while checkIfPossible(capacityLeft, orderQty):
		visited.append(nodeToVisit)
		allVisited.append(nodeToVisit)
		if nodeToVisit == None:
			break
		nodeToVisit, capacityLeft = findNextNode(graph[nodeToVisit], capacityLeft, orderQty, visited, allVisited)
		#visited.append(nodeToVisit)
		#allVisited.append(nodeToVisit)
	nodeToVisit = 0
	capacityLeft = capacity
	#print(visited)
	visited.pop()
	allPath.append(visited)
	visited = []

print(allPath)

path = []
for i in range(len(allPath)):
	curr = []
	for j in range(len(allPath[i])):
		if allPath[i][j] == 0:
			curr.append("r" + str(allPath[i][j]))
		else:
			curr.append("n" + str(allPath[i][j] - 1))
	curr.append("r0")
	path.append(curr)
#print(path)
	
path_dict = {}
for i in range(len(path)):
	path_dict["path" + str(i + 1)] = path[i]

json_object = {}
json_object["v0"] = path_dict

print(json_object)

with open("level1a_output.json", "w") as outfile:
    json.dump(json_object, outfile)

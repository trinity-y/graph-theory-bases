'''
bread first search
'''

# ADJACENCY LIST
#graphData[0] = # of nodes; graph[1] = # of edges
print("input # of nodes followed by # of edges")
graphData = list(map(int, input().split()))
adjList = [[] for i in range(graphData[0] + 1)]
print("input node neighbour pairs")
for i in range(graphData[1]):
	neighbourPair = list(map(int, input().split()))
	nodeA = neighbourPair[0]
	nodeB = neighbourPair[1]
	adjList[nodeA].append(nodeB)
	adjList[nodeB].append(nodeA)

#BREADTH FIRST SEARCH
def breadthFirstSearch(start):
	visited = [False for i in range(len(adjList))]
	visited[start] = True
	queue = [start]
	result = [start]
	while(len(queue)>0):
		currentNode = queue.pop(0)
		for neighbour in adjList[currentNode]:
			if visited[neighbour] == False:
				visited[neighbour] = True
				queue.append(neighbour)
				result.append(neighbour)
	return result

print(breadthFirstSearch(0))
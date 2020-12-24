'''
depth first search
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


#DEPTH FIRST SEARCH
visited = [False for i in range(len(adjList))]
result = []
def depthFirstSearch(node):
	result.append(node)
	visited[node] = True
	for neighbour in adjList[node]:
		if visited[neighbour] == False:
			depthFirstSearch(neighbour)
	return result

print(depthFirstSearch(int(input("which node do you want to start at?"))))
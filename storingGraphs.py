'''
adjacency matrix base
'''
# #graphData[0] = # of nodes; graph[1] = # of edges
print("input # of nodes followed by # of edges")
graphData = list(map(int, input("").split()))
#creates a graphData[0] x graphData[0] (not including 0 indexes) matrix filled with 0s
adjMatrix = [[0 for i in range(graphData[0] + 1)] for i in range(graphData[0] + 1)]
#take in neighbour pairs
print("input node neighbour pairs")
for i in range(graphData[1]):
	neighbours = list(map(int, input().split()))
	nodeA = neighbours[0]
	nodeB = neighbours[1]
	#sets the neighbouring pair coords to 1 in the matrix
	adjMatrix[nodeA][nodeB] = 1
	adjMatrix[nodeB][nodeA] = 1
print('\n'.join([' '.join(str(row)) for row in adjMatrix]))

'''
adjacency list base
'''
#graphData[0] = # of nodes; graph[1] = # of edges
print("input # of nodes followed by # of edges")
graphData = list(map(int, input().split()))
adjList = [[] for i in range(graphData[0] + 1)]
#take in neighbour pairs
print("input node neighbour pairs")
for i in range(graphData[1]):
	neighbourPair = list(map(int, input().split()))
	nodeA = neighbourPair[0]
	nodeB = neighbourPair[1]
	#adds the node name to it's neighbours list of adjacent nodes
	adjList[nodeA].append(nodeB)
	adjList[nodeB].append(nodeA)
print(adjList)



# I will be using a Python dictionary to act as an adjacency list
graph = {
  '1' : ['2','5'],
  '2' : ['3', '4'],
  '5' : ['6'],
  '3' : [],
  '4' : ['6'],
  '6' : []
}

visited = set() # this is a set data type used to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for DFS
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# calling the function while passing the start point
print("Following is the Depth-First Search")
dfs(visited, graph, '1')
# I will be using a Python dictionary to act as an adjacency list
graph = {
  '1' : ['2','5'],
  '2' : ['3', '4'],
  '5' : ['6'],
  '3' : [],
  '4' : ['6'],
  '6' : []
}

visited = [] # visited nodes.
queue = []     #setting a queue

def breadthFirstSearch(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

#calling the function while passing the start point
print("Following is the Breadth-First Search")
breadthFirstSearch(visited, graph, '1')
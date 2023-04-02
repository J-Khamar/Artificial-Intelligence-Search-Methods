def main():
  # Asking the user for the number of nodes and creating the graph.
  nodes = int(input("Enter number of nodes: "))
  print("<------------------------>")
  graph = create_graph(nodes)
  
  # Asking the user for the starting node and node we are searching for.
  start = input("Enter starting node: ")
  target = input("Enter target node: ")
  print("<------------------------>")

  # Applying breadth first search.
  bfs(graph, start, target)

def create_graph(nodes):
  # Creating an adjacency list using a dictionary.
  # Where the key is the node and the value is neigboring nodes.
  graph = {}
  for i in range(nodes):
    node = input("Enter node: ")
    graph[node] = input("Enter neighbors: ").split()
  print("<------------------------>")
  return graph

def bfs(graph, start, target):
  # Creating a list for the nodes visited and a queue to implemet the search.
  visited = [] 
  queue = []

  # Initialising the visited list and the queue with the starting node.
  visited.append(start)
  queue.append(start)

  # Looping through the queue till it is empty.
  while queue:
    current_node = queue.pop(0) 

    # We check if the current node is the target node and break the search if it is.
    if current_node == target:
      print(current_node)
      break
    print(current_node, end = "->") 

    # We remove the node at the front of the queue. 
    # We the and add itself and its neighbors to the visited list if they are not already there.
    for neighbor in graph[current_node]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)

if __name__ == "__main__":
  main()
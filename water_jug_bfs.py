def main():
    jug_a = int(input("Enter size of first jug: "))
    jug_b = int(input("Enter size of second jug: "))
    target = int(input("Enter target quantity: "))
    print("<--------------------------->")
    bfs(jug_a, jug_b, target)

def bfs(jug_a, jug_b, target):
    # Creating a list for the visied nodes, and a queue for bfs.
    # We initialise the queue with a (0, 0) tuple.
    visited = []
    queue = [(0, 0)]
    # We loop through the queue while it nost empty adding any ew nodes to the visited list.
    while queue:
        # We pop the tuple at the the front of the queue.
        current_a, current_b = queue.pop(0)
        # if the current node is already in visited we skip the iteration.
        if (current_a, current_b) in visited:
            continue
        # If not we add it to the visited list.
        visited.append((current_a, current_b))
        print(f"Visited: ({current_a}, {current_b})")
        # Checking if the goal coniditon is met.
        if current_a == target or current_b == target:
            print("<--------------------------->")
            print(f"Target quantity achieved: ({current_a}, {current_b})")
            return 

        # In the case of BFS we append all possible moves, i.e filling, emptying or pouring into jugs.
        queue.append((jug_a, current_b)) 
        queue.append((current_a, jug_b))
        queue.append((0, current_b)) 
        queue.append((current_a, 0))
        queue.append((min(current_a + current_b, jug_a), max(0, current_a + current_b - jug_a))) 
        queue.append((max(0, current_a + current_b - jug_b), min(current_a + current_b, jug_b))) 

if __name__ == "__main__":
  main()
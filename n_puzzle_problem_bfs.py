from collections import deque

def main():
    dimensions = int(input("Enter dimensions of the problem: "))
    print("Enter values for start matrix: ")
    initial_matrix = get_matrix(dimensions)
    print("Enter values for goal matrix: ")
    goal_matrix = get_matrix(dimensions)
    print("<--------------------------->")
    traversed, solution_path = bfs(initial_matrix, goal_matrix)
    traversed.pop(-1)
    if traversed != None:
        print("Nodes traversed:")
        for matrix in traversed:
            print(matrix)
        print("<--------------------------->")    
        print("Shortest path:")
        print(initial_matrix)
        for matrix in solution_path:
            print(matrix)

def get_matrix(n):
    # Taking inout from the user for the starting state.
    matrix = []
    # The matrix needs to be in numeric format hence why we have used the map function.
    for i in range(n):
        temp = input(f"Enter row {i + 1}: ").split(" ")
        matrix.append(list(map(int, temp)))
    return matrix

def generate_next_states(matrix):
    # Generates all possible next states for the given matrix 
    # By swapping the blank space (0) with its neighboring values.
    next_states = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i > 0:
                    up = [x[:] for x in matrix]
                    up[i][j], up[i - 1][j] = up[i - 1][j], up[i][j]
                    next_states.append(up)
                if i < len(matrix) - 1:
                    down = [x[:] for x in matrix]
                    down[i][j], down[i + 1][j] = down[i + 1][j], down[i][j]
                    next_states.append(down)
                if j > 0:
                    left = [x[:] for x in matrix]
                    left[i][j], left[i][j - 1] = left[i][j - 1], left[i][j]
                    next_states.append(left)
                if j < len(matrix[i]) - 1:
                    right = [x[:] for x in matrix]
                    right[i][j], right[i][j + 1] = right[i][j + 1], right[i][j]
                    next_states.append(right)
    return next_states

def bfs(matrix, goal_matrix):
    # Uses breadth-first search to find the solution 
    # By exploring all possible states and returning the solution when found.
    queue = deque([(matrix, [])])
    visited = [tuple(map(tuple, matrix))]
    while queue:
        current_matrix, path = queue.popleft()
        if current_matrix == goal_matrix:
            return visited, path
        for next_matrix in generate_next_states(current_matrix):
            if tuple(map(tuple, next_matrix)) not in visited:
                queue.append((next_matrix, path + [next_matrix]))
                visited.append(tuple(map(tuple, next_matrix)))
    return None

if __name__ == "__main__":
  main()
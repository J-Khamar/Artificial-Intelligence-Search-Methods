from collections import deque

def main():
    initial_matrix = get_matrix()
    print("<--------------------------->")
    if is_solvable(initial_matrix):
        traversed, solution_path = bfs(initial_matrix)
        traversed.pop(-1)
        if traversed != None:
            print("Nodes traversed:")
            for matrix in traversed:
                print(matrix)
            print("<--------------------------->")    
            print("Shortest path:")
            for matrix in solution_path:
                print(matrix)
    else:
        print("This puzzle is not solvable.")


def get_matrix():
    # Taking inout from the user for the starting state.
    matrix = []
    # The matrix needs to be in numeric format hence why we have used the map function.
    for i in range(2):
        temp = input(f"Enter row {i + 1}: ").split(" ")
        matrix.append(list(map(int, temp)))
    return matrix

def is_solvable(matrix):
    # checks if the given matrix is solvable 
    # By counting the number of inversions in the flat matrix and checking if it is even or odd.
    inversions = 0
    flat_matrix = [x for sublist in matrix for x in sublist]
    flat_matrix.remove(0)
    for i in range(len(flat_matrix)):
        for j in range(i  + 1, len(flat_matrix)):
            if flat_matrix[i] > flat_matrix[j]:
                inversions += 1
    return inversions % 2 == 0

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

def bfs(matrix):
    # Uses breadth-first search to find the solution 
    # By exploring all possible states and returning the solution when found.
    queue = deque([(matrix, [])])
    visited = [tuple(map(tuple, matrix))]
    while queue:
        current_matrix, path = queue.popleft()
        if current_matrix == [[1, 2], [3, 0]]:
            return visited, path
        for next_matrix in generate_next_states(current_matrix):
            if tuple(map(tuple, next_matrix)) not in visited:
                queue.append((next_matrix, path + [next_matrix]))
                visited.append(tuple(map(tuple, next_matrix)))
    return None

if __name__ == "__main__":
  main()
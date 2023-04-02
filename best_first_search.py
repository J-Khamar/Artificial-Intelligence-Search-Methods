import heapq

def main():
    print("Enter values for start matrix: ")
    initial_matrix = get_matrix()
    print("Enter values for goal matrix: ")
    goal_matrix = get_matrix()
    print("<--------------------------->")
    best_first_search(initial_matrix, goal_matrix)

def get_matrix():
    # Taking inout from the user for the starting state.
    matrix = []
    # The matrix needs to be in numeric format hence why we have used the map function.
    for i in range(3):
        temp = input(f"Enter row {i + 1}: ").split(" ")
        matrix.append(list(map(int, temp)))
    return matrix
    
def hamming_distance(config, goal):
    distance = 0
    for i in range(len(config)):
        for j in range(len(config[i])):
            if config[i][j] != goal[i][j] and config[i][j] != 0:
                distance += 1
    return distance

def best_first_search(init_config, goal_config):
    heap = []
    heapq.heappush(heap, (hamming_distance(init_config, goal_config), init_config, 0))
    visited = set()
    visited.add(tuple(map(tuple, init_config)))
    print("Initial State : ",init_config)
    while heap:
        state = heapq.heappop(heap)
        config, moves = state[1], state[2]

        if config == goal_config:
            return moves

        for next_config in generate_next_states(config):
            if tuple(map(tuple, next_config)) not in visited:
                heapq.heappush(heap, (hamming_distance(next_config, goal_config) + moves + 1, next_config, moves + 1))
                visited.add(tuple(map(tuple, next_config)))
                print("Visited State : ",next_config)

    return -1

def generate_next_states(config):
    next_states = []
    blank_x, blank_y = find_blank_tile(config)

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        x, y = blank_x + dx, blank_y + dy

        if x < 0 or x >= len(config) or y < 0 or y >= len(config[0]):
            continue

        next_config = [[val for val in row] for row in config]
        next_config[blank_x][blank_y], next_config[x][y] = next_config[x][y], next_config[blank_x][blank_y]

        next_states.append(next_config)

    return next_states

def find_blank_tile(config):
    for i in range(len(config)):
        for j in range(len(config[i])):
            if config[i][j] == 0:
                return i, j

if __name__ == "__main__":
  main()
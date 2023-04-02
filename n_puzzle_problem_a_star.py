import heapq

def main():
    size = int(input("Enter size of the puzzle matrix:"))

    print("Enter the start state: ")
    start = matrix_input(size)
    print("\nEnter the goal state: ")
    goal = matrix_input(size)

    a_star(start, goal)

def heuristic(config, goal):
    distance = 0
    for i in range(len(config)):
        for j in range(len(config[i])):
            if config[i][j] != goal[i][j] and config[i][j] != 0:
                distance += 1
    return distance

def a_star(start, goal):
    heap = []
    heapq.heappush(heap, (0, start, 0, heuristic(start, goal)))
    visited = set()
    visited.add(tuple(map(tuple, start)))
    print("State : ", start)
    while heap:
        state = heapq.heappop(heap)
        config, moves, cost, heur = state[1], state[2], state[0], state[3]

        if config == goal:
            return moves

        for next_config in generate_next_states(config):
            if tuple(map(tuple, next_config)) not in visited:
                f = cost + moves + 1 + heuristic(next_config, goal)
                heapq.heappush(
                    heap, (f, next_config, moves + 1, heuristic(next_config, goal)))
                visited.add(tuple(map(tuple, next_config)))
                print("State : ", next_config)
                if next_config == goal:
                    break
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
    return -1, -1

def matrix_input(size):
    matrix = []
    for i in range(size):
        temp = input(f"Enter row {i+1}: ").split(" ")
        matrix.append(list(map(int, temp)))
    return matrix

if __name__ == '__main__':
    main()
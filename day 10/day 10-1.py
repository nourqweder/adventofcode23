## The problem you're describing is a variation of the classic graph problem of finding the longest path in a graph. 
# However, it's important to note that finding the longest path in a graph is an NP-hard problem,
# and there's no efficient solution for arbitrary graphs.
# But in this case, the graph is a tree (since it's a loop with no cycles except the loop itself),
# and there's an efficient solution for trees. 
# The solution is to run BFS twice. 
# First, run BFS from the starting node to find the farthest node. 
# Then, run BFS from that farthest node to find the new farthest node.
# The distance to the new farthest node is the longest path in the tree.

from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([(root, 0)])  # Add a distance to the queue
    distances = {}
    while queue:
        vertex, distance = queue.popleft()
        visited.add(vertex)  # Mark the node as visited after it's popped from the queue
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append((neighbour, distance + 1))  # Increment the distance for each neighbour
                distances[neighbour] = distance + 1  # Store the distance
    return distances
def create_graph_and_find_start(grid):
    graph = {}
    start = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                graph[(i, j)] = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[i]) and grid[nx][ny] != '.':
                        graph[(i, j)].append((nx, ny))
            if grid[i][j] == 'S':
                start = (i, j)
    if start is None:
        raise ValueError("Starting position 'S' not found.")
    return graph, start

# Function to find the starting position 'S' in the grid
def find_starting_position(grid):
    # Loop over each row in the grid
    for i in range(len(grid)):
        # Loop over each column in the current row
        for j in range(len(grid[i])):
            # If the current cell is the starting position 'S'
            if grid[i][j] == 'S':
                # Return the coordinates of the starting position
                return i, j
    # If the starting position 'S' is not found, raise an error
    raise ValueError("Starting position 'S' not found.")

def find_starting_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return i, j
    raise ValueError("Starting position 'S' not found.")

def is_valid_move(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])
def find_farthest_distance(grid):
    graph, start = create_graph_and_find_start(grid)
    distances = bfs(graph, start)
    farthest_node = max(distances, key=distances.get)
    distances = bfs(graph, farthest_node)
    farthest_distance = max(distances.values())
    return farthest_distance

# Read the input from a file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

if __name__ == "__main__":
    file_path = "input.txt"  # Replace with the actual file path
    grid = read_input(file_path)

    try:
        result = find_farthest_distance(grid)
        print(f"The farthest distance along the loop is: {result}")
    except ValueError as e:
        print(e)

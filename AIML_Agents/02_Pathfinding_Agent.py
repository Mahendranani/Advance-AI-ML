# 02_Pathfinding_Agent.py
# -----------------------
# An agent that finds the shortest path using A* Algorithm.
# Heuristic: Manhattan Distance.

import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 # Cost from start to current node
        self.h = 0 # Heuristic (estimated cost from current to end)
        self.f = 0 # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    heapq.heappush(open_list, start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares (no diagonals)

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            # Manhattan distance heuristic
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child == open_node and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)
            
    return None # No path found

def main():
    # 0 = Walkable, 1 = Wall
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    print("--- Pathfinding Agent (A*) ---")
    print(f"Start: {start}")
    print(f"End: {end}")
    
    path = astar(maze, start, end)
    
    if path:
        print("\nPath found:")
        print(path)
        
        # Visualize
        print("\nVisualization (S=Start, E=End, *=Path, #=Wall):")
        for i in range(len(maze)):
            row_str = ""
            for j in range(len(maze[0])):
                if (i, j) == start:
                    row_str += "S "
                elif (i, j) == end:
                    row_str += "E "
                elif (i, j) in path:
                    row_str += "* "
                elif maze[i][j] == 1:
                    row_str += "# "
                else:
                    row_str += ". "
            print(row_str)
    else:
        print("No path found")

if __name__ == '__main__':
    main()

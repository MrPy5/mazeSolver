class Node:
    def __init__(self, x, y, char="*"):

        self.char = char
        self.x = x
        self.y = y

    def update(self,maze):
        global solved
        global end_node_coords
        if (maze[self.y][self.x+1] == " " or maze[self.y][self.x+1] == "B") and self.x + 1 < len(maze[0]):
            if maze[self.y][self.x+1] == "b":
                solved = True
                end_node_coords = [self.x, self.y]
            else:
                node = Node(self.x+1, self.y, ">")
                node_list.append(node)

        if (maze[self.y][self.x-1] == " " or maze[self.y][self.x-1] == "B") and self.x - 1 >= 0:
            if maze[self.y][self.x - 1] == "b":
                solved = True
                end_node_coords = [self.x, self.y]
            else:

                node = Node(self.x - 1, self.y, "<")

                node_list.append(node)

        if (maze[self.y+1][self.x] == " " or maze[self.y+1][self.x] == "B") and self.y + 1 < len(maze):
            if maze[self.y+1][self.x] == "b":
                solved = True
                end_node_coords = [self.x, self.y]

            else:

                node = Node(self.x, self.y+1, "v")

                node_list.append(node)
        if (maze[self.y-1][self.x] == " " or maze[self.y-1][self.x] == "B") and self.y - 1 >= 0:
            if maze[self.y - 1][self.x] == "b":
                solved = True
                end_node_coords = [self.x, self.y]
            else:
                node = Node(self.x, self.y - 1, "^")
                node_list.append(node)


class Holder():
    def __init__(self, nodes=[]):
        self.nodes = nodes
    def add_node(self, node):
        self.nodes.append(node)

def print_maze(maze):

    for row in maze:
        print(row)

def place_in_maze(maze, x, y, char):

    row = maze[y]
    row = row[:x] + char + row[x+1:]
    maze[y] = row
    return maze

def solve(maze, start_char, end_char):
    global node_list
    global holding_list
    global start
    global end
    global solved
    global end_node_coords
    solved = False
    end_char = end_char
    end_node_coords = []
    print_maze(maze)
    input()

    node_list = []
    holding_list = []
    start = [0, 0]

    x, y = 0, 0

    for row in maze:
        for char in row:
            if char == start_char:
                start = [x, y]
                print(start)
            y += 1
        x += 1
        y = 0



    x, y = 0, 0
    for row in maze:
        for char in row:
            if char == end_char:
                end = [x, y]

            y += 1
        x += 1
        y = 0


    node = Node(start[0], start[1], start_char)


    node_list.append(node)


    while not solved:
        for node in node_list:

            node.update(maze)
            maze = place_in_maze(maze, node.x, node.y, node.char)
            if solved:
                for node in node_list:
                    maze = place_in_maze(maze, node.x, node.y, node.char)
                break
        for node in node_list:

            maze = place_in_maze(maze, node.x, node.y, node.char)

        print_maze(maze)
        if solved:
            break

    print(end_node_coords)


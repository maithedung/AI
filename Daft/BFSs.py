# Đề bài: không gian trạng thái bt 1
#   0 1 2 3 4 5 6 7 8
#
#   S A B C D E F G H
# S 0 1 1 1 0 0 0 0 0
# A 1 0 0 0 1 0 0 0 0
# B 1 0 0 0 1 1 0 1 0
# C 1 0 0 0 0 1 0 0 0
# D 0 1 0 0 0 0 1 0 0
# E 0 0 1 1 0 0 1 0 1
# F 0 0 0 0 1 1 0 1 0
# G 0 0 1 0 0 0 1 0 1
# H 0 0 0 0 0 1 0 1 0
def read_file(file_path):
    f = open(file_path)
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    data = []
    for line in lines:
        data.append([int(num) for num in line.split(" ")])
    return data


def map_data_to_tree(tree, data):
    for idx, row in enumerate(data):
        tree.add_node(node_name=idx)
        for idx_col, col in enumerate(row):
            if col == 1:
                tree.add_edge(start_name=idx, end_name=idx_col)


class Node:
    def __init__(self, data):
        self.data = data
        self.parents = []
        self.children = []

    def get_data(self):
        return self.data

    def get_children(self):
        return [node.get_data() for node in self.children]

    def get_parents(self):
        return [node.get_data() for node in self.parents]


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def clear(self):
        self.nodes = []
        self.edges = []

    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return len(self.edges)

    def get_index(self, node):
        for idx, n in enumerate(self.nodes):
            if n.get_data() == node.get_data():
                return idx
        return -1

    def add_node(self, node_name):
        node = Node(node_name)
        if not self.is_contains(node):
            self.nodes.append(node)

    def add_node_from(self, array_of_nodes_name):
        for el in array_of_nodes_name:
            node = Node(el)
            if not self.is_contains(node):
                self.nodes.append(node)

    def is_contains(self, node):
        for el in self.nodes:
            if el.get_data() == node.get_data():
                return True
        return False

    def add_edge(self, start_name, end_name):
        start_node = Node(start_name)
        end_node = Node(end_name)
        if not self.is_contains(start_node):
            self.add_node(start_name)
        if not self.is_contains(end_node):
            self.add_node(end_name)
        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)
        self.nodes[start_index].children.append(end_node)
        self.nodes[end_index].parents.append(start_node)
        self.edges.append((self.nodes[start_index], self.nodes[end_index]))

    def add_edges_from(self, array_of_tuple_node):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            self.add_edge(start, end)

    def show_nodes(self):
        return [node.get_data() for node in self.nodes]

    def show_edges(self):
        return [(edge[0].get_data(), edge[1].get_data()) for edge in self.edges]


def Breadth_First_Search(tree, initialState, goalTest):
    # start_node = Node(initialState)
    # end_node = Node(destinationState)
    frontier = []
    frontier.append(initialState)
    explored = []
    while len(frontier) > 0:
        print("Frontier >> ", frontier)
        state = frontier.pop(0)
        state_node = Node(state)
        explored.append(state)
        # print("Explored >> ", explored)
        if goalTest == state:
            return True
        index_state = tree.get_index(state_node)
        for neighbor in tree.nodes[index_state].get_children():
            if neighbor not in list(set(frontier + explored)):
                frontier.append(neighbor)
    return False


if __name__ == "__main__":
    tree = Tree()
    # # From file
    # data = read_file("bfs.txt")
    # map_data_to_tree(tree, data)
    # result = bfs(tree, 0, 7)
    # print(result)
    # -----------------------------------------------------
    # Add Node manually
    tree.add_node("S")
    tree.add_node_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
    print(tree.show_nodes())
    tree.add_edges_from(
        [
            ("S", "A", 3),
            ("S", "B", 6),
            ("S", "C", 2),
            ("A", "D", 3),
            ("B", "G", 9),
            ("B", "E", 2),
            ("C", "E", 1),
            ("D", "F", 5),
            ("E", "H", 5),
            ("F", "E", 6),
            ("H", "G", 8),
            ("F", "G", 5),
        ]
    )
    result = Breadth_First_Search(tree, "S", "G")
    print(result)

class Node:
    COST = '__COST__'
    GOAL_COST = '__GOAL_COST__'
    A_STAR = '__A_STAR__'

    def __init__(self, label, cost=100000, goal_cost=100000):
        self.label = label
        self.cost = cost  # for uniform cost search
        self.goal_cost = goal_cost  # for greedy best fit search
        self.compare_mode = Node.COST  # set compare mode for specific algorithm
        self.path = []
        self.parents = []
        self.children = []
        self.depth = 0

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal_cost": self.goal_cost,
        }))

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.compare_mode is Node.COST:
            return self.cost < other.cost
        if self.compare_mode is Node.GOAL_COST:
            return self.goal_cost < other.goal_cost
        if self.compare_mode is Node.A_STAR:
            return self.cost + self.goal_cost < other.cost + other.goal_cost
        return self.cost < other.cost

    def get_label(self):
        return self.label

    def get_children(self):
        return [node.get_label() for node in self.children]

    def get_parents(self):
        return [node.get_label() for node in self.parents]

    def get_neighbors(self):
        return [node.get_label() for node in self.neighbors()]

    def neighbors(self):
        children = self.children
        parents = self.parents
        neigbors = children + parents
        seen = set()
        neigbors = [x for x in children +
                    parents if not (x in seen or seen.add(x))]
        return neigbors

    def set_compare_mode(self, mode):
        if mode != Node.COST and mode != Node.A_STAR and mode != Node.GOAL_COST:
            self.compare_mode = Node.COST
        else:
            self.compare_mode = mode


class Graph:
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
            if n == node:
                return idx
        return -1

    def is_contains(self, node):
        for el in self.nodes:
            if el == node:
                return True
        return False

    def add_node(self, label):
        node = Node(label)
        if not self.is_contains(node):
            self.nodes.append(node)

    def add_node_from(self, array_of_label):
        for el in array_of_label:
            self.add_node(label=el)
    """
        add edge with weight of edge
    """

    def add_edge(self, start_label, end_label, weight=10000):
        start_node = Node(start_label)
        end_node = Node(end_label)
        if not self.is_contains(start_node):
            self.add_node(start_node)
        if not self.is_contains(end_node):
            self.add_node(end_node)
        # get index to create constraints parent and children
        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)
        self.nodes[start_index].children.append(self.nodes[end_index])
        self.nodes[end_index].parents.append(self.nodes[start_index])
        # create edge between 2 nodes created
        self.edges.append(
            (self.nodes[start_index], self.nodes[end_index], weight))
    """
        array_of_tuple_node ('A', 'B', weight)
        is_duplicate: accept create 2 direction of edge (default is 1)
    """

    def add_edges_from(self, array_of_tuple_node, is_duplicated=False):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            if len(tup) == 3:
                weight = tup[2] or 10000
            else:
                # if no weight is pass, default weight is 10000
                weight = 10000
            self.add_edge(start, end, weight)
            if is_duplicated:
                self.add_edge(end, start, weight)
    """
         get edge between 2 node
    """

    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node
                    and edges[1] == end_node][0]
        except:
            return None
    """
        show list of node label
    """

    def show_nodes(self):
        return [node.get_label() for node in self.nodes]
    """
        show list of edge containing 2 node and weight
    """

    def show_edges(self):
        return [(edge[0].get_label(), edge[1].get_label(), edge[2]) for edge in self.edges]

    def set_compare_mode(self, mode):
        for node in self.nodes:
            node.set_compare_mode(mode)

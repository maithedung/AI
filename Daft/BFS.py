import Queue


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []


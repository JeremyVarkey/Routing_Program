class Graph:

    #  consider making it a nested dict, because that way we can quickly find what is our starting vertex
    def __init__(self):
        # No need to have adjacency list since all destinations connect to each other
        self.edges = dict()

    def add_directed_edge(self, a, b, weight):
        self.edges[(a, b)] = weight

    def add_undirected_edge(self, a, b, weight):
        self.add_directed_edge(a, b, weight)
        self.add_directed_edge(b, a, weight)

    def print_contents(self):
        for key, value in self.edges.items():
            print('{0} : {1}'.format(key, value))


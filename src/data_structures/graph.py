class Graph:
    def __init__(self):
        self._nodes = {}
        self._adjacency_list = {}

    def add_node(self, node_id, data):
        if node_id in self._nodes:
            return
        self._nodes[node_id] = data
        self._adjacency_list[node_id] = []

    def add_edge(self, source, target, weight=1.0, bidirectional=True):
        if source not in self._nodes or target not in self._nodes:
            raise ValueError("Nodes must exist first for both source and target!!!")

        edge = {"target": target, "weight": weight}
        self._adjacency_list[source].append(edge)

        if bidirectional:
            reverse_edge = {"target": source, "weight": weight}
            self._adjacency_list[target].append(reverse_edge)

    def get_edges(self, node_id):
        return self._adjacency_list.get(node_id, [])

    def exists(self, node_id):
        return node_id in self._nodes

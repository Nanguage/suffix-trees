from graphviz import Digraph


def node_label(node):
    label = "{}, {}".format(node.idx, node.depth)
    return label


class VisualizeTree():

    def __init__(self, stree):
        self.stree = stree
        self.nodes = set()
        self.edges = set()
        self.stree.root._traverse(self._read_tree)

    def _read_tree(self, node):
        self.nodes.add(node)
        targets = [n for n, _ in node.transition_links]
        for t in targets:
            self.nodes.add(t)
            if t is not node:
                self.edges.add((node, t))

    def to_graphviz(self):
        dot = Digraph()
        for n in self.nodes:
            if n.is_leaf():
                dot.node(node_label(n), _attributes={"shape": "box"})
            else:
                dot.node(node_label(n))

        for s, t in self.edges:
            edge_label = self.stree._edgeLabel(t, s)
            s_, t_ = node_label(s), node_label(t)
            dot.edge(s_, t_, label=edge_label)

        return dot


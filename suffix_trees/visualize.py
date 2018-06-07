from graphviz import Digraph


def node_label(node):
    if node.idx == 0 and node.depth == 0:
        return "root"
    if node.is_leaf():
        idx = node.idx
    else:
        idx = chr(97+node.idx)
    label = "{}, {}".format(idx, node.depth)
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

    def remove_edge_multi_end(self, label):
        words = self.stree.words
        if words is not None:
            first_sym = words[0][-1]
            first_sym_idx = label.find(first_sym)
            if first_sym_idx != -1:
                return label[:first_sym_idx+1]
        return label

    def to_graphviz(self, remove_multi_end=True):
        dot = Digraph()
        for n in self.nodes:
            if n.is_leaf():
                dot.node(node_label(n), _attributes={"shape": "box"})
            else:
                dot.node(node_label(n))

        for s, t in self.edges:
            edge_label = self.stree._edgeLabel(t, s)
            if remove_multi_end:
                edge_label = self.remove_edge_multi_end(edge_label)
            s_, t_ = node_label(s), node_label(t)
            dot.edge(s_, t_, label=edge_label)

        return dot


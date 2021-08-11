class Node:
    def __init__(self, parent=None, data=0, wordEnd=False):
        self.child_nodes = [None] * 26
        self.parent_node = parent
        self.data = data
        self.isWordEnd = wordEnd
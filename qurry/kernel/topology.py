class Topology:
    def __init__(self, size, mapping=None):
        self.size = size
        if mapping is not None:
            self.mapping = mapping
        else:
            self.mapping = dict()

    def valid(self, a, b):
        return b in self.mapping[a]

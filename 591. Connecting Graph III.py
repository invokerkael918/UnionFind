class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        self.count = n
        for i in range(1, n + 1):
            self.father[i] = i

    def connect(self, a, b):
        # write your code here
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.count -= 1
            self.father[rootA] = rootB

    def find(self, node):
        path = []

        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node

    """
    @return: An integer
    """

    def query(self):
        # write your code here
        return self.count

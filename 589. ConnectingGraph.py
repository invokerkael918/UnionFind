class ConnectingGraph:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        for i in range(1, n + 1):
            self.father[i] = i

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """

    def query(self, a, b):
        # write your code here
        return self.find(a) == self.find(b)

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node

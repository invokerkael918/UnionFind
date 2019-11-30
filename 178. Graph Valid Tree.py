class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False

        self.father = {}
        self.count = n
        for i in range(n):
            self.father[i] = i

        for pair in edges:
            self.connect(pair[0], pair[1])

        else:
            return self.count == 1

    def connect(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.count -= 1
            self.father[rootA] = rootB

    def find(self, node):
        path = []

        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node
        return node

class ConnectingGraph2:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        self.size = {}
        for i in range(1, n + 1):
            self.father[i] = i
            self.size[i] = 1

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if (root_a != root_b):
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    """
    @param: a: An integer
    @return: An integer
    """

    def query(self, a):
        # write your code here
        root_a = self.find(a)
        return self.size[root_a]

    def find(self, x):
        j = x
        fx = 0
        while (self.father[j] != j):
            j = self.father[j]
        while (x != j):
            fx = self.father[x]
            self.father[x] = j
            x = fx
        return j

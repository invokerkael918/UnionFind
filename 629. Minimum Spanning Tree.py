class Solution:
    # @param {Connection[]} connections given a list of connections include two cities and cost
    # @return {Connection[]} a list of connections from results
    """
    (1) 按距离对edge进行排序
    (2) 循环，把所有城市初始化，父节点设置为自己，累加计数器
    (3) 循环，对每个edge进行union操作；如果不属于同一个区域，则联通并将count减1，并将这个edge加入结果
    (4) 如果最终所有区域连在一起，则count = 1，返回results； 否则返回空数组
    """
    def lowestCost(self, connections):
        if not connections or len(connections) == 0:
            return []

        self.father = {}
        self.count = 0
        results = []
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))

        for connection in connections:
            for city in (connection.city1, connection.city2):
                if city not in self.father:
                    self.father[city] = city
                    self.count += 1

        for connection in connections:
            if self.union(connection.city1, connection.city2):
                results.append(connection)

        if self.count == 1:
            return results
        return []

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        self.father[root_b] = root_a
        self.count -= 1
        return True

    def find(self, city):
        path = []
        while self.father[city] != city:
            path.append(city)
            city = self.father[city]
        for c in path:
            self.father[c] = city

        return city
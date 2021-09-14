class Graph:
    
    def __init__(self, graph_struct = {}):

        self.graph = graph_struct

    def __str__(self):

        grh = ''
        for vrt in self.getVertices():
            for adj in self.getAdjacent(vrt):
                grh += '({0}, {1}, {2})\t'.format(vrt, adj, self.graph[vrt][adj])
        return grh

    def setVertex(self, vertex):

        if vertex not in self.graph.keys():
            self.graph[vertex] = {}
        return self

    def setAdjacent(self, vertex, adj, weight=0):

        if vertex not in self.graph.keys():
            self.graph[vertex] = {}
        if adj not in self.graph.keys():
            self.graph[adj] = {}
        
        self.graph[vertex][adj] = weight
        self.graph[adj][vertex] = weight
        return self
    
    def getVertices(self):

        return list(self.graph.keys())

    def getAdjacent(self, vertex):

        if vertex in self.graph.keys():
            return self.graph[vertex]

    def getPathCost(self, path):
        
        pathCost = 0
        for vrt, adj in zip(path, path[1:]):
            pathCost += self.graph[vrt][adj]
        return pathCost


